import streamlit as st
from llama_index.core.schema import Document
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.core.node_parser import SentenceSplitter
from backend.config import DATA_PATH, CHUNK_OVERLAP, CHUNK_SIZE, CHAT_MEMORY_TOKEN_LIMIT,LLM_SYSTEM_PROMPT, SIMILARITY_TOP_K
from llama_index.core.memory import ChatMemoryBuffer
from backend.engine.components import get_embedding_model, initialise_llm
from backend.engine.engine import get_chat_engine
from llama_index.core.chat_engine.types import BaseChatEngine

# for rag_engine
from backend.engine.components import get_embedding_model, initialise_llm
from backend.engine.engine import get_chat_engine

# 2. version
#@st.cache_resource
def init_bot(local=False):
    print("--- Initialising RAG system 😎... ---")
    llm = initialise_llm()
    embed_model = get_embedding_model()
    chat_engine = get_chat_engine(llm=llm, embed_model=embed_model)
    print("--- RAG Chatbot Initialised. ---")
    return chat_engine

# Make UI into a function
def render_chatbot_page(chat_engine):
    st.title("📘 Welcome to a world where help becomes growth")
    st.image(
        "https://cdn-icons-png.flaticon.com/512/1041/1041916.png",
        width=100,
        caption="Your Assistant 🤖"
    )

    st.markdown("A space where technology meets the human soul — discover your inner universe 💫")

    # Display chat history
    for message in chat_engine.chat_history:
        with st.chat_message(message.role):
            st.markdown(message.blocks[0].text)

    # User input
    if prompt := st.chat_input("Ask me anything about the inner world..."):
        st.chat_message("human").markdown(prompt)

        with st.spinner("Thinking... 🤔"):
            answer = chat_engine.chat(prompt)
            response = answer.response

            with st.chat_message("assistant"):
                st.markdown(response)






# # 1. version 
# @st.cache_resource
# def init_bot(local=False):

#     #return build_chat_engine(local)

#     print("--- Initialising RAG system 😎... ---")
#     llm = initialise_llm()
#     embed_model = get_embedding_model()

#     chat_engine = get_chat_engine(llm=llm, embed_model=embed_model)
#     print("--- RAG Chatbot Initialised. ---")
#     return chat_engine # NOICE: we are not using .chat_repl()

# rag_bot = init_bot()

# ################## Streamlit UI ##################
# st.title("📘 Wellcome to the inner World")
# st.image(
#     "https://cdn-icons-png.flaticon.com/512/1041/1041916.png",
#    # "https://cdn-icons-png.flaticon.com/512/4712/4712037.png", 
#     width=100,
#     caption="Your Assistant 🤖"
# )

# st.markdown("A space where technology meets the human soul — discover your inner universe 💫")

# # Display chat messages from history
# for message in rag_bot.chat_history:
#     with st.chat_message(message.role):
#         st.markdown(message.blocks[0].text)

# # User input
# if prompt := st.chat_input("Ask me anything about the inner world..."):
#     st.chat_message("human").markdown(prompt)

#     with st.spinner("Thinking... 🤔"):
#         answer = rag_bot.chat(prompt)
#         response = answer.response

#         with st.chat_message("assistant"):
#             st.markdown(response)


# RUN THE PROGRAM OF LIVE LIBRARY AND CHATBOT OF GPT
# conda activate live_library
# cd backend
# streamlit run homepage.py
# or streamlit run chatbot_rag_engine.py


# RUN THE RAG_ENGINE SEPARATE WITH THE PROGRAM OF LIVE LIBRARY
# not be in the folder backend
# conda activate live_library
# or streamlit run app.py
