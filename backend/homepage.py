# LIVE_LIBRARY_24_7/backend/layout_homepage.py
import streamlit as st
import pandas as pd
from sqlalchemy import text
from database import engine
from layout_css import apply_branchlayout, apply_layout_footer
from main import administrative_page

# Import branch pages
# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(page_title="Live Library Management 24/7", page_icon="📚", layout="wide")
apply_branchlayout()

# -------------------------------------------------
# SESSION NAVIGATION
# -------------------------------------------------
if "current_page" not in st.session_state:
    st.session_state.current_page = "home"

# Function to navigate to a different page
def go_to(page_name: str):
    # reset any expert selection when changing pages
    st.session_state.selected_expert = None
    st.session_state.current_page = page_name

# -------------------------------------------------
# HOME PAGE CONTENT
# -------------------------------------------------
if st.session_state.current_page == "home":
    st.markdown("<div class='section'>", unsafe_allow_html=True)
    st.markdown("<h1>Welcome to <span style='color:#19e526;'>Live Library Management 24/7 </span></h1>", unsafe_allow_html=True) # #2563eb
    st.write("Discover, manage, learn, and transform through courses, coaching, and live sessions with global experts.")


    # -------------------------------------------------
    # BRANCHES SECTION
    # -------------------------------------------------
    st.markdown("<h2 style='text-align:center;'><br></h2>", unsafe_allow_html=True)
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT branch_name, description FROM branches LIMIT 4;"))
            branches = result.fetchall()
        # begin: Display branches as cards
        if branches:
            icons = ["🧘", "💪", "💬", "💰"]
            cols = st.columns(4)
            for i, branch in enumerate(branches):
                with cols[i]:
                    # Each card triggers navigation
                    if st.button(f"{icons[i]} {branch.branch_name.title()}"):
                        go_to(branch.branch_name.lower())
                    st.markdown(f"""
                    <div class="branch-card">
                        <p>{branch.description}</p>
                    </div>
                    """, unsafe_allow_html=True)

        else:
            st.warning("⚠️ No branches found in database.")
    except Exception as e:
        st.error(f"Database error: {e}")

    st.markdown("<div class='section_buttons'>", unsafe_allow_html=True)
    col1, col2 = st.columns([1,1])

    left_col, _ = st.columns([2, 4])  # left column + empty space to keep them on the left

    with left_col:
        st.markdown("### ⚙️ Management Tools")  # optional small header

        if st.button("📚 Analytic Management"):
            go_to("analytics")   # ✅ Navigate to analytics page

        st.write("")  # small vertical space between buttons

        if st.button("🚀 Administrative Management"):
            go_to("administrative")   # ✅ Navigate to admin page


    apply_layout_footer()

# -------------------------------------------------
# PAGE ROUTING LOGIC
# -------------------------------------------------
else:   
    administrative_page()
    
