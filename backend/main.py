# backend/main.py
import sys
from pathlib import Path    
import streamlit as st
from fastapi import FastAPI

# --- ensure backend folder is importable ---
sys.path.append(str(Path(__file__).resolve().parent))

from branch_template import show_branch_by_name
from visualize_courses import show_visualize_courses
from administrative_template import show_admin_page
from homepage import render_homepage, go_to

# -------------------------------------------------
# 3️⃣ Initialize FastAPI app
# -------------------------------------------------

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Backend API is running!"}


def administrative_page():
    # if st.session_state.current_page == "inner":
    #     # style inner page
    #     show_branch_by_name("inner", "🧘", "Inner Self & Mindfulness")

    # elif st.session_state.current_page == "health":
    #     show_branch_by_name("health", "💪", "Physical and Mental Health")

    # elif st.session_state.current_page in ["social", "relationship"]:
    #     show_branch_by_name("social", "💬", "Relationship & Social Harmony")

    # elif st.session_state.current_page == "finance":
    #     show_branch_by_name("finance", "💰", "Finance & Career Empowerment")

    # elif st.session_state.current_page == "analytics":
    #     show_visualize_courses()
    
    # elif st.session_state.current_page == "administrative":
    #     show_admin_page()

    if st.session_state.current_page == "home":
        render_homepage()

    elif st.session_state.current_page == "inner":
        show_branch_by_name("inner", "🧘", "Inner Self & Mindfulness")

    elif st.session_state.current_page == "health":
        show_branch_by_name("health", "💪", "Physical and Mental Health")

    elif st.session_state.current_page in ["social", "relationship"]:
        show_branch_by_name("social", "💬", "Social and Family Relationship")

    elif st.session_state.current_page == "finance":
        show_branch_by_name("finance", "💰", "Finance & Career Empowerment")

    elif st.session_state.current_page == "analytics":
        show_visualize_courses()
    
    elif st.session_state.current_page == "administrative":
        show_admin_page()

# extra functionality for administrative page to control permissions for delete/edit/create of courses
    # elif st.session_state.current_page == "administrative":
    #     # permission model:
    #     # - admin: CRUD all courses; can Delete; optional toggle to show "expert-style" panel
    #     # - expert: CRU only on own courses (no Delete)
    #     # - participant: no admin page (guard)
    #     if role == "participant":
    #         st.warning("You don't have permission to access the Administrative page.")
    #         if st.button("⬅️ Back to Home"):
    #             go_to("home")
    #     else:
    #         can_delete = (role == "admin")
    #         restrict_to_user = (role == "expert")
    #         show_admin_page(
    #             role=role,
    #             user_id=user_id,
    #             can_delete=can_delete,
    #             restrict_to_user=restrict_to_user
    #         )






# -------------------------------------------------
# 5️⃣ Example route to verify API works
# -------------------------------------------------
@app.get("/")
def root():
    return {"message": "✅ Backend is running and connected!"}


