import sys
project_root_dir = "/Users/annaphuong/Downloads/Final_project/121125/live_library_247"
sys.path.append(project_root_dir)

from pathlib import Path
from ragas.metrics import (
    ContextPrecision,
    ContextRecall,
    Faithfulness,
    ResponseRelevancy,
)

# --- Paths for Evaluation ---
#EVALUATION_ROOT_PATH: Path = Path('/Users/annaphuong/Downloads/Final_project/121125/live_library_247/evaluation/eval_config.py') # Path(__file__).parent
#EVALUATION_RESULTS_PATH: Path = EVALUATION_ROOT_PATH / "evaluation_results/"
#EXPERIMENTAL_VECTOR_STORES_PATH: Path = Path('/Users/annaphuong/Downloads/Final_project/121125/live_library_247/evaluation/eval_config.py').parent.parent / "local_storage" / "experimental_vector_stores/"


# EXPERIMENTAL_VECTOR_STORES_PATH: Path = Path(__file__).parent.parent / "local_storage" / "experimental_vector_stores/"

# --- Paths for Evaluation ---
EVALUATION_ROOT_PATH: Path = Path(__file__).parent
EVALUATION_RESULTS_PATH: Path = EVALUATION_ROOT_PATH / "evaluation_results/"
EXPERIMENTAL_VECTOR_STORES_PATH: Path = Path(__file__).parent.parent / "local_storage" / "experimental_vector_stores/"



# --- Ragas Evaluation Metrics ---
EVAL_METRICS = [
    Faithfulness(),
    # ResponseRelevancy(),
    ContextPrecision(),
    ContextRecall(),
]
EVAL_METRICS