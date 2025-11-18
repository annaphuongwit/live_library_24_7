from llama_index.core.chat_engine import SimpleChatEngine
from backend.config import LLM_SYSTEM_PROMPT
from backend.engine.components import initialise_llm
from llama_index.llms.groq import Groq
from llama_index.core import (
    StorageContext,
    SimpleDirectoryReader,
    VectorStoreIndex,
    load_index_from_storage,
)
from llama_index.core.chat_engine.types import BaseChatEngine
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.schema import Document
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.groq import Groq

from backend.config import (
    CHUNK_OVERLAP,
    CHUNK_SIZE,
    DATA_PATH,
    LLM_SYSTEM_PROMPT,
    SIMILARITY_TOP_K,
    VECTOR_STORE_PATH,
    CHAT_MEMORY_TOKEN_LIMIT,
)
from backend.engine.components import get_embedding_model, initialise_llm

def main_chat_loop_memory() -> None:
    """Main chat loop for a conversational chatbot."""
    llm: Groq = initialise_llm()

    # Create a chat engine using the system prompt
    conversation = SimpleChatEngine.from_defaults(
        llm=llm,
        system_prompt=LLM_SYSTEM_PROMPT
    )

    print("--- Chat Started ---")
    print("Type 'exit' or 'quit' to end the conversation.")
    print("--------------------")
    conversation.chat_repl()

#Step1: Creating the vector store

def _create_new_vector_store(embed_model: HuggingFaceEmbedding) -> VectorStoreIndex:
    """Creates, saves, and returns a new vector store from documents."""
    print("Creating new vector store from all files in the 'data' directory...")

    # This reads all the text files in the specified directory.
    documents: list[Document] = SimpleDirectoryReader(input_dir=DATA_PATH).load_data()

    if not documents:
        raise ValueError(f"No documents found in {DATA_PATH}. Cannot create vector store.")

    # This breaks the long document into smaller, more manageable chunks.
    text_splitter: SentenceSplitter = SentenceSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    # This is the core of the vector store. It takes the text chunks,
    # uses the embedding model to convert them to vectors, and stores them.
    index: VectorStoreIndex = VectorStoreIndex.from_documents(
        documents,
        transformations=[text_splitter],
        embed_model=embed_model
    )

    # This saves the newly created index to disk for future use.
    index.storage_context.persist(persist_dir=VECTOR_STORE_PATH.as_posix())
    print("Vector store created and saved.")
    return index

#Step2: Loading the vector store

def get_vector_store(embed_model: HuggingFaceEmbedding) -> VectorStoreIndex:
    """Loads the vector store from disk if it exists; otherwise, creates a new one."""
    # Create the parent directory if it doesn't exist.
    VECTOR_STORE_PATH.mkdir(parents=True, exist_ok=True)

    # Check if the directory contains any files.
    if any(VECTOR_STORE_PATH.iterdir()):
        print("Loading existing vector store from disk...")
        storage_context = StorageContext.from_defaults(persist_dir=VECTOR_STORE_PATH.as_posix())
         #We must provide the embed_model when loading the index.
        return load_index_from_storage(storage_context, embed_model=embed_model)
    else:
        # If the directory is empty, call our internal function to build the index.
        return _create_new_vector_store(embed_model)
    
    #step3: Assembling the RAG Chat Engine
def get_chat_engine(llm: Groq, embed_model: HuggingFaceEmbedding) -> BaseChatEngine:
    """Initialises and returns the main conversational RAG chat engine."""
    vector_index: VectorStoreIndex  = get_vector_store(embed_model)
    memory: ChatMemoryBuffer = ChatMemoryBuffer.from_defaults(token_limit=CHAT_MEMORY_TOKEN_LIMIT)

    # Assemble the RAG chat engine
    chat_engine: BaseChatEngine  = vector_index.as_chat_engine(
        chat_mode="context",
        memory=memory,
        llm=llm,
        system_prompt=LLM_SYSTEM_PROMPT,
        similarity_top_k=SIMILARITY_TOP_K,
    )
    return chat_engine

#step 4: The Main application Loop

def main_chat_loop() -> None:
    """Main application loop to run the RAG chatbot."""
    print("--- Initialising models... ---")
    llm: Groq = initialise_llm()
    embed_model: HuggingFaceEmbedding = get_embedding_model()

    chat_engine: BaseChatEngine = get_chat_engine(llm=llm, embed_model=embed_model)
    print("--- RAG Chatbot Initialised. ---")
    chat_engine.chat_repl()





#######################################
# if __name__ == "__main__":
#     main_chat_loop()
# import os
# from llama_index.core.llms import CompletionResponse
# from llama_index.llms.groq import Groq

# from backend.config import LLM_QUESTION
# from backend.engine.components import initialise_llm

# def main_chat_loop() -> None:
#     """Main chat loop to ask a question to the LLM and print the answer."""

#     llm: Groq = initialise_llm()

#     api_key = os.getenv("GROQ_API_KEY")

#     # answer: CompletionResponse = llm.complete(LLM_QUESTION)

#     # Start the conversation loop
#     while True:
#         user_input = input("You 😎 (note: saying 'end' ends the chat ‼️): ")

#         # Check for exit condition
#         if user_input.lower() == "end": # USER= 'eNd'
#         # if user_input.upper() == "END": USER= 'eNd'

#             print("Ending the conversation. Goodbye!")
#             break

#         # Get the response from the conversation chain
#         response = llm.complete(user_input)

#         # Print the chatbot's response
#         # print(response)

#         # print(f"Question: {LLM_QUESTION}")
#         print("-------------------")
#         print(f"Answer 💁: {response}")

# there is no memory here






# from llama_index.core.chat_engine import SimpleChatEngine
# from backend.config import LLM_SYSTEM_PROMPT
# from backend.engine.components import initialise_llm
# from llama_index.llms.groq import Groq
# from llama_index.core import (
#     StorageContext,
#     SimpleDirectoryReader,
#     VectorStoreIndex,
#     load_index_from_storage,
# )
# from llama_index.core.chat_engine.types import BaseChatEngine
# from llama_index.core.memory import ChatMemoryBuffer
# from llama_index.core.node_parser import SentenceSplitter
# from llama_index.core.schema import Document
# from llama_index.embeddings.huggingface import HuggingFaceEmbedding
# from llama_index.llms.groq import Groq

# from backend.config import (
#     CHUNK_OVERLAP,
#     CHUNK_SIZE,
#     DATA_PATH,
#     LLM_SYSTEM_PROMPT,
#     SIMILARITY_TOP_K,
#     VECTOR_STORE_PATH,
#     CHAT_MEMORY_TOKEN_LIMIT,
# )
# from backend.engine.components import get_embedding_model, initialise_llm

# def main_chat_loop_memory() -> None:
#     """Main chat loop for a conversational chatbot."""
#     llm: Groq = initialise_llm()

#     # Create a chat engine using the system prompt
#     conversation = SimpleChatEngine.from_defaults(
#         llm=llm,
#         system_prompt=LLM_SYSTEM_PROMPT
#     )

#     print("--- Chat Started ---")
#     print("Type 'exit' or 'quit' to end the conversation.")
#     print("--------------------")
#     conversation.chat_repl()

# #Step1: Creating the vector store

# def _create_new_vector_store(embed_model: HuggingFaceEmbedding) -> VectorStoreIndex:
#     """Creates, saves, and returns a new vector store from documents."""
#     print("Creating new vector store from all files in the 'data' directory...")

#     # This reads all the text files in the specified directory.
#     documents: list[Document] = SimpleDirectoryReader(input_dir=DATA_PATH).load_data()

#     if not documents:
#         raise ValueError(f"No documents found in {DATA_PATH}. Cannot create vector store.")

#     # This breaks the long document into smaller, more manageable chunks.
#     text_splitter: SentenceSplitter = SentenceSplitter(
#         chunk_size=CHUNK_SIZE,
#         chunk_overlap=CHUNK_OVERLAP
#     )

#     # This is the core of the vector store. It takes the text chunks,
#     # uses the embedding model to convert them to vectors, and stores them.
#     index: VectorStoreIndex = VectorStoreIndex.from_documents(
#         documents,
#         transformations=[text_splitter],
#         embed_model=embed_model
#     )

#     # This saves the newly created index to disk for future use.
#     index.storage_context.persist(persist_dir=VECTOR_STORE_PATH.as_posix())
#     print("Vector store created and saved.")
#     return index

# #Step2: Loading the vector store

# def get_vector_store(embed_model: HuggingFaceEmbedding) -> VectorStoreIndex:
#     """Loads the vector store from disk if it exists; otherwise, creates a new one."""
#     # Create the parent directory if it doesn't exist.
#     VECTOR_STORE_PATH.mkdir(parents=True, exist_ok=True)

#     # Check if the directory contains any files.
#     if any(VECTOR_STORE_PATH.iterdir()):
#         print("Loading existing vector store from disk...")
#         storage_context = StorageContext.from_defaults(persist_dir=VECTOR_STORE_PATH.as_posix())
#          #We must provide the embed_model when loading the index.
#         return load_index_from_storage(storage_context, embed_model=embed_model)
#     else:
#         # If the directory is empty, call our internal function to build the index.
#         return _create_new_vector_store(embed_model)
    
#     #step3: Assembling the RAG Chat Engine
# def get_chat_engine(llm: Groq, embed_model: HuggingFaceEmbedding) -> BaseChatEngine:
#     """Initialises and returns the main conversational RAG chat engine."""
#     vector_index: VectorStoreIndex  = get_vector_store(embed_model)
#     memory: ChatMemoryBuffer = ChatMemoryBuffer.from_defaults(token_limit=CHAT_MEMORY_TOKEN_LIMIT)

#     # Assemble the RAG chat engine
#     chat_engine: BaseChatEngine  = vector_index.as_chat_engine(
#         chat_mode="context",
#         memory=memory,
#         llm=llm,
#         system_prompt=LLM_SYSTEM_PROMPT,
#         similarity_top_k=SIMILARITY_TOP_K,
#     )
#     return chat_engine

# #step 4: The Main application Loop

# def main_chat_loop() -> None:
#     """Main application loop to run the RAG chatbot."""
#     print("--- Initialising models... ---")
#     llm: Groq = initialise_llm()
#     embed_model: HuggingFaceEmbedding = get_embedding_model()

#     chat_engine: BaseChatEngine = get_chat_engine(llm=llm, embed_model=embed_model)
#     print("--- RAG Chatbot Initialised. ---")
#     chat_engine.chat_repl()


    
        