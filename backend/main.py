# backend/routers.py
import streamlit as st
from  branch_template import show_branch_by_name
from visualize_courses import show_visualize_courses
from administrative_template import show_admin_page

def administrative_page():
    if st.session_state.current_page == "inner":
        # Bechtle-style inner page
        show_branch_by_name("inner", "🧘", "Inner Self & Mindfulness")

    elif st.session_state.current_page == "health":
        show_branch_by_name("health", "💪", "Physical and Mental Health")

    elif st.session_state.current_page in ["social", "relationship"]:
        show_branch_by_name("social", "💬", "Relationship & Social Harmony")

    elif st.session_state.current_page == "finance":
        show_branch_by_name("finance", "💰", "Finance & Career Empowerment")

    elif st.session_state.current_page == "analytics":
        show_visualize_courses()
    
    elif st.session_state.current_page == "administrative":
        show_admin_page()


# def go_back_to_home():
#     #st.markdown("---")
#     if st.button("⬅️ Back to Home"):
#         st.session_state.selected_expert = None
#         st.session_state.current_page = "home"
