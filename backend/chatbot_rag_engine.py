# -------------------------------------------------------
# Live Library 24/7 — RAG Chatbot (Dynamic Corpus Loader)
# -------------------------------------------------------
from __future__ import annotations
import math, re, os
from collections import Counter
from typing import List, Dict
import streamlit as st
from sqlalchemy import text

# ---------- Database connection ----------
try:
    from database import engine
except Exception:
    from sqlalchemy import create_engine
    engine = create_engine("mysql+pymysql://root:Sonne1!#@localhost:3306/live_library_manage_system")

# ---------- Text helpers ----------
TOKEN_RE = re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ\u00C0-\u1EF9]+", re.UNICODE)

def tokenize(text: str) -> List[str]:
    return [t.lower() for t in TOKEN_RE.findall(text or "")]

def tf(tokens: List[str]) -> Dict[str, float]:
    c = Counter(tokens)
    n = float(sum(c.values())) or 1.0
    return {k: v / n for k, v in c.items()}

def idf(all_docs: List[List[str]]) -> Dict[str, float]:
    N = len(all_docs) or 1
    df = Counter()
    for toks in all_docs:
        for t in set(toks):
            df[t] += 1
    return {t: math.log((N + 1) / (dfv + 1)) + 1.0 for t, dfv in df.items()}

def vec(tf_map: Dict[str, float], idf_map: Dict[str, float]) -> Dict[str, float]:
    return {k: v * idf_map.get(k, 0.0) for k, v in tf_map.items()}

def cosine(a: Dict[str, float], b: Dict[str, float]) -> float:
    if not a or not b:
        return 0.0
    dot = sum(a.get(k, 0.0) * b.get(k, 0.0) for k in set(a) | set(b))
    na = math.sqrt(sum(v * v for v in a.values()))
    nb = math.sqrt(sum(v * v for v in b.values()))
    return (dot / (na * nb)) if na and nb else 0.0



# ---------- Dynamic RAG Corpus Loader ----------
def load_corpus_from_files(base_dir: str | None = None) -> Dict[str, Dict[str, List[str]]]:
    """
    Dynamically load all .txt files from backend/data directory.
    File naming pattern:
        _branch_language.txt
        Example: _inner_understand_english.txt → branch=inner, language=English
    """
    # ✅ Determine the correct folder: backend/data/
    if base_dir is None:
        current_dir = os.path.dirname(__file__)
        base_dir = os.path.join(current_dir, "data")

    corpus: Dict[str, Dict[str, List[str]]] = {}

    # Ensure the directory exists
    if not os.path.exists(base_dir):
        print(f"⚠️ Data folder not found: {base_dir}")
        return corpus

    # Iterate through all .txt files inside backend/data/
    for file in os.listdir(base_dir):
        if file.endswith(".txt") and file.startswith("_"):
            parts = file.replace(".txt", "").strip("_").split("_")
            if len(parts) < 2:
                continue
            branch = parts[0].lower()
            language = parts[-1].capitalize()
            path = os.path.join(base_dir, file)

            try:
                with open(path, "r", encoding="utf-8") as f:
                    content = [line.strip() for line in f.readlines() if line.strip()]
                corpus.setdefault(branch, {}).setdefault(language, []).extend(content)
            except Exception as e:
                print(f"⚠️ Could not read {file}: {e}")

    print(f"✅ Loaded corpus for {len(corpus)} branches from {base_dir}")
    return corpus


# Load corpus dynamically from backend/data/
CORPUS = load_corpus_from_files()





# def load_corpus_from_files(base_dir: str = os.path.dirname(__file__)) -> Dict[str, Dict[str, List[str]]]:
#     corpus: Dict[str, Dict[str, List[str]]] = {}
#     for file in os.listdir(base_dir):
#         if file.endswith(".txt") and file.startswith("_"):
#             # Example: _inner_understand_english.txt → branch = inner, language = English
#             parts = file.replace(".txt", "").strip("_").split("_")
#             if len(parts) < 2:
#                 continue
#             branch = parts[0].lower()
#             language = parts[-1].capitalize()
#             path = os.path.join(base_dir, file)

#             try:
#                 with open(path, "r", encoding="utf-8") as f:
#                     content = [line.strip() for line in f.readlines() if line.strip()]
#                 corpus.setdefault(branch, {}).setdefault(language, []).extend(content)
#             except Exception as e:
#                 print(f"⚠️ Could not read {file}: {e}")
#     return corpus


# # Load corpus dynamically
# CORPUS = load_corpus_from_files()


# ---------- RAG logic ----------
def get_supported_languages() -> List[str]:
    try:
        with engine.connect() as conn:
            rows = conn.execute(text("SELECT DISTINCT language FROM countries ORDER BY language")).fetchall()
        langs = [r[0] for r in rows if r[0]]
        known = set(sum([list(CORPUS[b].keys()) for b in CORPUS], []))
        return [l for l in langs if l in known] or ["English"]
    except Exception:
        return list({l for b in CORPUS.values() for l in b.keys()}) or ["English"]

def build_index(branch: str, language: str):
    docs = CORPUS.get(branch, {}).get(language, [])
    tok_docs = [tokenize(d) for d in docs]
    idf_map = idf(tok_docs) if tok_docs else {}
    vecs = [vec(tf(t), idf_map) for t in tok_docs]
    return docs, idf_map, vecs

def retrieve(branch: str, language: str, query: str, k: int = 3):
    docs, idf_map, vecs = build_index(branch, language)
    if not docs:
        return []
    qv = vec(tf(tokenize(query)), idf_map)
    scored = [(cosine(qv, v), d) for v, d in zip(vecs, docs)]
    return sorted(scored, key=lambda x: x[0], reverse=True)[:k]

def synthesize_answer(branch: str, language: str, query: str) -> str:
    hits = retrieve(branch, language, query)
    if not hits:
        return "I couldn’t find relevant info yet. Try switching language or rephrasing your question."
    bullets = "\n".join([f"• {p}" for _, p in hits])
    return (
        f"**{branch.title()} | {language}**\n\n"
        f"\n{bullets}\n\n"
        f"💡 *Try one small action today and reflect afterwards.*"
    )


# ---------- Streamlit UI ----------
def show_chatbot():
   # st.subheader("🤖 Live Library Chatbot")
   
    col1, col2 = st.columns(2)
    with col1:
        branches = sorted(list(CORPUS.keys())) or ["inner", "health", "social", "finance"]
        branch = st.selectbox("Select branch", branches, index=0)
    with col2:
        langs = sorted(list(CORPUS.get(branch, {}).keys()))
        language = st.selectbox("Select language", langs, index=0 if langs else 0)

    st.divider()
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # render chat history
    for role, msg in st.session_state.chat_history:
        with st.chat_message(role):
            st.markdown(msg)

    # user input
    user_prompt = st.chat_input("Type your question...")
    if user_prompt:
        st.session_state.chat_history.append(("user", user_prompt))
        with st.chat_message("user"):
            st.markdown(user_prompt)

        with st.chat_message("assistant"):
            answer = synthesize_answer(branch, language, user_prompt)
            st.markdown(answer)
        st.session_state.chat_history.append(("assistant", answer))


# ---------- Run standalone ----------
if __name__ == "__main__":
    show_chatbot()




