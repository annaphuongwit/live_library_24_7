# backend/homepage.py
import sys
from pathlib import Path
#sys.path.append(str(Path(__file__).resolve().parent))
# --- Allow import from project root where app.py is ---
ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

import streamlit as st
from app import init_bot, render_chatbot_page  # <-- Now this works
from sqlalchemy import text
from database import engine
from layout_css import apply_branchlayout, apply_layout_footer #,show_navibar
from _auth import require_login, logout_button, register_ui
from branch_template import show_branch_by_name
from visualize_courses import show_visualize_courses
from administrative_template import show_admin_page
#from chatbot_rag_engine import show_chatbot


# ---------------------------
# Page config + base styles
# ---------------------------
st.set_page_config(page_title="Live Library 24/7", page_icon="📚", layout="wide")
apply_branchlayout()

# ---------------------------
# Initialize session state
# ---------------------------
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"
if "selected_expert" not in st.session_state:
    st.session_state.selected_expert = None

# ---------------------------
# Navigation helper
# ---------------------------
def go_to(page_name: str):

    st.session_state.selected_expert = None
    st.session_state.current_page = page_name
    # ⚠️ do NOT rerun immediately — Streamlit will rerun automatically after button press
    # st.experimental_rerun()

# ---------------------------
# Auth + role
# ---------------------------
user = require_login()
if not user:
    st.stop()

logout_button()
role = (user.get("role") or "").lower()
user_id = user.get("user_id")

# =====================================================
# 🌐 NAVBAR FUNCTION
# =====================================================

def show_navbar():
    current = st.session_state.current_page

    # ---- Navbar Layout ----
    col1, col2, col3, col4, col5 = st.columns([2, 1, 1, 1, 1])
    with col1:
        st.markdown("<div class='nav-title'>📚 Live Library 24/7</div>", unsafe_allow_html=True)
    with col2:
        if st.button("🏠 Home", key="nav_home", help="Go to Home",
                     use_container_width=True) or current == "home":
            if st.session_state.current_page != "home":
                go_to("home")
    with col3:
        if st.button("📊 Analytic", key="nav_analytic", help="Visualize data",
                     use_container_width=True):
            go_to("analytics")
    with col4:
        if st.button("⚙️ Administrative", key="nav_admin", help="Manage data",
                     use_container_width=True):
            go_to("administrative")
    with col5:
        if st.button("💬 Help Center", key="nav_help", help="Ask the chatbot",
                 use_container_width=True):

            if "chatbot_engine" not in st.session_state:
                st.session_state["chatbot_engine"] = init_bot(local=False)

            go_to("chatbot")
    # with col5:
    #     if st.button("💬 Help Center", key="nav_help", help="Ask the chatbot",
    #                  use_container_width=True):
    #         go_to("chatbot")
    
    


# ---------------------------
# Page Router
# ---------------------------

def render_homepage():
    show_navbar()
    current = st.session_state.current_page
    
    # ===== 1️⃣ HOME PAGE =====
    if current == "home":
     
        # ---------------------------------------
        # 🧩 Custom Navbar Layout
        # ---------------------------------------
        

        st.markdown("<div class='section'>", unsafe_allow_html=True)
        st.markdown(
            "<h1>Welcome to <span style='color:#19e526;'>Live Library Management 24/7</span></h1>",
            unsafe_allow_html=True,
        )
        st.write("Discover, manage, learn, and transform through courses, coaching, and live sessions with global experts.")
    
        # ---- Branch cards ----
        try:
            with engine.connect() as conn:
                branches = conn.execute(text("SELECT branch_name, description FROM branches LIMIT 4;")).fetchall()
            if branches:
                icons = ["🧘", "💪", "💬", "💰"]
                cols = st.columns(4)
                for i, branch in enumerate(branches):
                    with cols[i]:
                        if st.button(f"{icons[i]} {branch.branch_name.title()}"):
                            go_to(branch.branch_name.lower())
                        st.markdown(
                            f"""
                            <div class="branch-card">
                                <p>{branch.description}</p>
                            </div>
                            """,
                            unsafe_allow_html=True,
                        )
            else:
                st.warning("⚠️ No branches found in the database.")
        except Exception as e:
            st.error(f"Database error: {e}")

        # # ---- Management Tools ----
        # if role in ("expert", "admin"):
        #     st.markdown("### ⚙️ Management Tools")
        #     if st.button("📊 Analytic Management"):
        #             go_to("analytics")
        
        #     if st.button("🚀 Administrative Management"):
        #             go_to("administrative")



    # ===== 2️⃣ BRANCH PAGES =====
    elif current == "inner":
        show_branch_by_name("inner", "🧘", "Inner Self & Mindfulness")
    elif current == "health":
        show_branch_by_name("health", "💪", "Physical and Mental Health")
    elif current == "social":
        show_branch_by_name("social", "💬", "Social and Family Relationship")
    elif current == "finance":
        show_branch_by_name("finance", "💰", "Finance and Career Empowerment")
    elif current == "register":
        register_ui()
    # ===== 3️⃣ ANALYTICS PAGE =====
    elif current == "analytics":
        show_visualize_courses()

    # ===== 4️⃣ ADMIN PAGE =====
    elif current == "administrative":
        show_admin_page(
            role=role,
            user_id=user_id,
            can_delete=(role == "admin"),
            restrict_to_user=(role == "expert"),
        )

    # ===== 5️⃣ HELP CENTER PAGE =====
    elif current == "chatbot":
        bot = st.session_state.get("chatbot_engine")

        # 🔥 Use app.py's UI directly
        render_chatbot_page(bot)
#     elif current == "chatbot":
#         st.image(
#     "https://cdn-icons-png.flaticon.com/512/1041/1041916.png",
#     width=100,
#     caption="Chatbot Help Center"
# )
#         #st.markdown("## 💬 Live Library Help Center !!!!")
#         st.caption("Ask the assistant any question — Inner, Health, Social, or Finance.")
#         show_chatbot()

    # ===== fallback =====
    else:
        st.warning("Unknown page — returning to Home.")
        st.session_state.current_page = "home"

    # apply_layout_footer()





# ---------------------------
# Run app
# ---------------------------
if __name__ == "__main__" or True:
    render_homepage()


# RUN THE PROGRAM OF LIVE LIBRARY AND CHATBOT OF GPT
# conda activate live_library
# cd backend
# streamlit run homepage.py
# or streamlit run chatbot_rag_engine.py


# RUN THE RAG_ENGINE SEPARATE WITH THE PROGRAM OF LIVE LIBRARY
# not be in the folder backend
# conda activate live_library
# or streamlit run app.py


