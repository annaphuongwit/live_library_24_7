import sys
project_root_dir = "/Users/annaphuong/Downloads/Final_project/121125/live_library_247"
sys.path.append(project_root_dir)

from datetime import datetime

from datasets import Dataset
from llama_index.core import (
    SimpleDirectoryReader,
    StorageContext,
    VectorStoreIndex,
    load_index_from_storage)

from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.query_engine import BaseQueryEngine
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq

import pandas as pd

from ragas import evaluate

from evaluation.eval_config import (
    EVAL_METRICS,
    EVALUATION_RESULTS_PATH,
    EXPERIMENTAL_VECTOR_STORES_PATH,
)

from evaluation.evaluation_questions import EVAL_DATA

from backend.config import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    DATA_PATH,
    SIMILARITY_TOP_K,
)
from backend.engine.components import get_embedding_model, initialise_llm


# 1 getting evaluation data
def get_eval_data() -> tuple[list[str], list[str]]:
    """Extracts questions and ground truths from the EVAL_DATA constant."""
    return [item["question"] for item in EVAL_DATA], [item["ground_truth"] for item in EVAL_DATA]

# 2 building or loading an experimental index
# Load the vector store if exists otherwise build it

def get_or_build_index(
    chunk_size: int,
    chunk_overlap: int,
    embed_model: HuggingFaceEmbedding
) -> VectorStoreIndex:
    """
    Checks for a persisted vector store for this experiment.
    If it exists, it loads it. If not, it builds it, persists it, and returns it.
    """
    vector_store_id: str = f"vs_baseline"
    specific_vector_store_path: Path = EXPERIMENTAL_VECTOR_STORES_PATH / vector_store_id

    if specific_vector_store_path.exists():

        #pointing to index files: knows where is saved index files (docstore, vectorstore, indexstore) via persist_dir
        print(f"--- Loading existing index from: {vector_store_id} ---")
        storage_context: StorageContext = StorageContext.from_defaults(
            persist_dir=str(specific_vector_store_path)
        )

        # rebuilds an in-memory VectorStoreIndex object from already-persisted storage
        # looks inside that persisted folder, reads the stored metadata, docstore, and embeddings,
        # and reconstructs a VectorStoreIndex object in memory.
        # The embed_model is passed in so the index knows how to generate/query embeddings in a consistent way with what was stored
        index: VectorStoreIndex = load_index_from_storage(
            storage_context,
            embed_model=embed_model
        )
    else:
        # Creating Index files from the Alice in Wonderland book
        print(f"--- Creating new index for: {vector_store_id} ---")
        documents: list[Document] = SimpleDirectoryReader(input_dir=DATA_PATH).load_data()

        text_splitter: SentenceSplitter = SentenceSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        index: VectorStoreIndex = VectorStoreIndex.from_documents(
            documents,
            transformations=[text_splitter],
            embed_model=embed_model
        )
        # presisting the index files to hard-desk
        index.storage_context.persist(persist_dir=str(specific_vector_store_path))
        print(f"--- Saved new index to: {vector_store_id} ---")
    return index

# 3 generating the question-answer dataset
def generate_qa_dataset(
    query_engine: BaseQueryEngine,
    questions: list[str],
    ground_truths: list[str]
) -> Dataset:
    """
    Generates answers and contexts for a given query engine and returns a HuggingFace Dataset.
    """
    responses: list[str] = []
    contexts: list[list[str]] = []
    for question in questions:
        print(f"Querying for question: '{question[:50]}...'")
        response_object = query_engine.query(question)
        responses.append(str(response_object))
        # the 4 chunks that were retrieved
        contexts.append([node.get_content() for node in response_object.source_nodes])

    response_data: dict[str, list[Any]] = {
        "question": questions,
        "answer": responses,
        "contexts": contexts,
        "ground_truth": ground_truths,
    }
    return Dataset.from_dict(response_data)


# def generate_qa_dataset_2(
#     query_engine: BaseQueryEngine,
#     questions: list[str],
#     ground_truths: list[str]
# ) -> Dataset:
#     responses: list[str] = []
#     contexts: list[list[str]] = []

#     for question in questions:
#         response_object = query_engine.query(question)
#         responses.append("" if response_object is None else str(response_object))

#         nodes = getattr(response_object, "source_nodes", [])
#         if not nodes:
#             contexts.append([""])  # placeholder
#         else:
#             contexts.append([str(node.get_content()) for node in nodes])

#     # ensure same length
#     assert len(questions) == len(responses) == len(contexts) == len(ground_truths)

#     response_data = {
#         "question": questions,
#         "answer": responses,
#         "contexts": contexts,
#         "ground_truth": ground_truths,
#     }

#     return Dataset.from_dict(response_data)

# 4 saving the result
def save_results(
    results_df: pd.DataFrame,
    filename_prefix: str
) -> None:
    """Saves the evaluation results and summary to CSV files."""
    results_dir: Path = EVALUATION_RESULTS_PATH # '/Users/annaphuong/Downloads/Final_project/121125/live_library_247/evaluation/evaluation_results'
    print("EVALUATION_RESULTS_PATH", f'{EVALUATION_RESULTS_PATH}')
    results_dir.mkdir(exist_ok=True, parents=True)
    timestamp: str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

    detailed_path: Path = results_dir / f"{filename_prefix}_detailed_{timestamp}.csv"
    # the detailed csv
    results_df.to_csv(detailed_path, index=False)
    print(f"\\n--- 💾 Detailed results saved to {detailed_path} ---")

    summary_path: Path = results_dir / f"{filename_prefix}_summary_{timestamp}.csv"
    param_cols: list[str] = [
        col
        for col in ['chunk_size', 'chunk_overlap']
        if col in results_df.columns
    ]
    if param_cols:
        # the summary csv
        avg_scores: pd.DataFrame = results_df.groupby(param_cols).mean(numeric_only=True)
        avg_scores.to_csv(summary_path)
        print(f"--- 💾 Summary of average scores saved to {summary_path} ---")


# 5 the Main evaluation function
def evaluate_baseline(
    llm: Groq,
    embed_model: HuggingFaceEmbedding
) -> pd.DataFrame:
    """Evaluates the RAG system using the baseline settings from config.py."""
    print("\n--- 🚀 Stage 1: Evaluating Baseline Configuration ---")
    questions, ground_truths = get_eval_data()

    index: VectorStoreIndex = get_or_build_index(
        chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP, embed_model=embed_model
    )
    # chat engine from the vector DB to get the responses
    query_engine: BaseQueryEngine = index.as_query_engine(similarity_top_k=SIMILARITY_TOP_K, llm=llm)

    qa_dataset: Dataset = generate_qa_dataset(query_engine, questions, ground_truths)

    print("--- Running Ragas evaluation for baseline... ---")
    result: Dataset = evaluate(
        dataset=qa_dataset,
        metrics=EVAL_METRICS,
        raise_exceptions=True,
    )

    results_df: pd.DataFrame = result.to_pandas()
    results_df['chunk_size'] = CHUNK_SIZE
    results_df['chunk_overlap'] = CHUNK_OVERLAP

    save_results(results_df, "baseline_evaluation")
    print("--- ✅ Baseline Evaluation Complete ---")
    return results_df


if __name__ == "__main__":
    llm_to_test: Groq = initialise_llm()
    embed_model_to_test: HuggingFaceEmbedding = get_embedding_model()

    evaluate_baseline(llm=llm_to_test, embed_model=embed_model_to_test)