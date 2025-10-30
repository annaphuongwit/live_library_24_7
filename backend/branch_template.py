# backend/branch_template.py
import streamlit as st
import pandas as pd
from sqlalchemy import text
from database import engine
from layout_css import apply_branchlayout, apply_layout_footer

def show_branch_by_name(branch_key: str, branch_icon: str, branch_title: str):
    """Column-style two-column layout for a branch page."""
    apply_branchlayout()

    st.markdown(f"<h1>{branch_icon} <span style='color:#19e526;'>{branch_title} </span></h1>", unsafe_allow_html=True)
    st.caption("Explore expert-led sessions, live learning, and personal growth opportunities.")
    st.markdown("---")

    # 2 columns like Bechtle
    col_left, col_right = st.columns([1.2, 2.8])

    # ───────── LEFT: Experts ─────────
    with col_left:
        st.subheader("👩‍🏫 Experts")

        try:
            with engine.connect() as conn:
                # Call the stored procedure for this branch
                query = text("CALL proc_get_experts_and_active_courses_by_branch(:branch_name);")
                experts_df = pd.read_sql(query, conn, params={"branch_name": branch_key})
        except Exception as e:
            st.error(f"Database error loading experts: {e}")
            st.stop()

        # Reset selected expert if page first loaded
        if "selected_expert" not in st.session_state:
            st.session_state.selected_expert = None

        if experts_df.empty:
            st.info("No experts available for this branch.")
        else:
            # "Show all" first
            if st.button("📜 Show All Courses", key=f"all_{branch_key}"):
                st.session_state.selected_expert = None

            # Display experts as clickable cards/buttons
            for i, expert in experts_df.iterrows():
                expert_name = expert["Expert_Name"]
                rating = expert["Expert_Rating"]
                courses = expert["Active_Courses"] if expert["Active_Courses"] else "No active courses"

                if st.button(f"⭐ {expert_name} ({float(rating):.1f})", key=f"exp_{branch_key}_{i}"):
                    st.session_state.selected_expert = expert_name

                if st.session_state.selected_expert == expert_name:
                    st.markdown(f"**Courses:** {courses}")
                    st.markdown("---")


    
    # ───────── RIGHT: Courses ─────────
    with col_right:
        st.subheader("📚 Courses")

        selected_expert = st.session_state.get("selected_expert", None)

        try:
            with engine.connect() as conn:
                if selected_expert:
                    # Use new procedure for expert-specific courses
                    query = text("CALL proc_get_courses_by_branch_and_expert(:branch_name, :expert_name);")
                    df = pd.read_sql(query, conn, params={
                        "branch_name": branch_key,
                        "expert_name": selected_expert
                    })
                else:
                    # Show all active courses by branch
                    df = pd.read_sql(
                        text("CALL proc_get_active_courses_by_branch(:bname);"),
                        conn,
                        params={"bname": branch_key}
                    )
        except Exception as e:
            st.error(f"Database error loading courses: {e}")
            st.stop()


        if df.empty:
            st.info("No active courses found.")
        else:
            # --- make columns robust (case/space/underscore-insensitive) ---
            def norm(s: str) -> str:
                return "".join(s.lower().replace("_", "").split())

            # build a lookup from normalized name -> real column name
            col_lookup = {norm(str(c)): str(c) for c in df.columns}

            def pick(row, *names, default="—"):
                """Return the first existing column value among candidate names."""
                for name in names:
                    k = norm(name)
                    if k in col_lookup:
                        return row[col_lookup[k]]
                return default

            # (Optional) you can inspect what columns came back:
            # st.caption(f"Columns: {list(df.columns)}")

            for _, row in df.iterrows():
                title    = pick(row, "Title", "course_title", default="Untitled Course")
                coach    = pick(row, "Coacher", "Coach", "ExpertName", "expert_name", default="Unknown")
                lang     = pick(row, "Language", "Lang", default="N/A")
                rating   = pick(row, "Rating", "avg_rating", default="N/A")
                price    = pick(row, "Price", default="N/A")
                desc     = pick(row, "Description", "Desc", default="")
                students = pick(row, "Students", "TotalStudents", "Total_Students", "Total Students", "num_students", default="—")
                link     = pick(row, "Link", "connect_link", default="")

                # make rating pretty if it's Decimal
                try:
                    rating = f"{float(rating):.1f}"
                except Exception:
                    pass

                link_html = f"<a href='{link}' target='_blank' style='color:#2563eb;'>🔗 Join Live Session</a>" if str(link).strip() else ""

                st.markdown(f"""
                <div class="branch-card" style="text-align:left; margin-bottom:1rem;">
                    <h3 style="color:#2563eb; margin-bottom:0.3rem;">{title}</h3>
                    <p><b>Coach:</b> {coach} &nbsp;&nbsp; | &nbsp;&nbsp;
                       <b>Language:</b> {lang} &nbsp;&nbsp; | &nbsp;&nbsp;
                       <b>Rating:</b> ⭐ {rating}</p>
                    <p>{desc}</p>
                    <p><b>Price:</b> €{price} &nbsp;&nbsp; <b>Students:</b> {students}</p>
                    {link_html}
                </div>
                """, unsafe_allow_html=True)

    st.markdown("---")
    if st.button("⬅️ Back to Home", key=f"back_{branch_key}"):
        # also clear selection when going home
        st.session_state.selected_expert = None
        st.session_state.current_page = "home"

    apply_layout_footer()
