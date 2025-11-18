# backend/chatbot_bootstrap.py
from backend.engine.components import get_embedding_model, initialise_llm
from backend.engine.engine import get_chat_engine

def build_chat_engine(local: bool = False):
    llm = initialise_llm()
    embed_model = get_embedding_model()
    return get_chat_engine(llm=llm, embed_model=embed_model)
