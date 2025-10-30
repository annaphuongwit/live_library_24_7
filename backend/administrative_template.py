# frontend/administrative_management.py
import streamlit as st
import pandas as pd
from sqlalchemy import text
from database import engine
from layout_css import apply_layout_scrollable_box


def show_admin_page():
    st.set_page_config(page_title="🚀 Administrative Management", page_icon="🛠️", layout="wide")
    st.markdown("<h1 style='font-size:2.1rem; color:#333;'>🚀 <span style='color:#19e526;'>Administrative Management</span></h1>", unsafe_allow_html=True)
    st.caption("Manage all expert courses: create, update, and delete directly from this dashboard.")

    # Back button
    if st.button("⬅️ Back to Home"):
        st.session_state.current_page = "home"
        st.stop()

    # ----------------------------------------
    # 1️⃣ Load data
    # ----------------------------------------
    try:
        with engine.connect() as conn:
            df = pd.read_sql(text("SELECT * FROM view_current_courses_status;"), conn)
    except Exception as e:
        st.error(f"Database connection error: {e}")
        st.stop()

    if df.empty:
        st.warning("No course data available.")
        st.stop()

    df.columns = [c.strip().replace(" ", "_") for c in df.columns]

    # ----------------------------------------
    # 2️⃣ Expert search box
    # ----------------------------------------
    st.markdown("---")
    st.markdown("<h3 style='color:#19e526;'>🔍 Search Expert and Manage Courses</h3>", unsafe_allow_html=True)

    expert_list = sorted(df["Expert"].unique().tolist())

    expert_input = st.text_input("Enter expert name:", "", key="admin_search_box")

    filtered_df = df
    matched_experts = []

    def normalize_name(name: str):
        return name.replace(".", "").strip().lower()

    if expert_input.strip():
        expert_input_norm = normalize_name(expert_input)
        matched_experts = [name for name in expert_list if normalize_name(name).startswith(expert_input_norm)]

        if matched_experts:
            st.success(f"✅ Total {len(matched_experts)} expert(s):")
            st.write(", ".join(matched_experts))
            exact_match = [x for x in matched_experts if normalize_name(x) == expert_input_norm]
            if len(exact_match) == 1:
                selected_expert = exact_match[0]
                st.info(f"📊 Showing all courses for **{selected_expert}**")
                filtered_df = df[df["Expert"].apply(lambda x: normalize_name(x)) == expert_input_norm]
                st.session_state.selected_expert = selected_expert
            else:
               # st.warning("Showing combined results for all matched experts.")
                filtered_df = df[df["Expert"].apply(lambda x: normalize_name(x)).isin([normalize_name(x) for x in matched_experts])]
        else:
            st.warning("No matching expert found.")
    else:
        st.info("Showing all experts' courses.")

    # ----------------------------------------
    # 3️⃣ Display filtered table
    # ----------------------------------------
    st.markdown("---")
    box_height = apply_layout_scrollable_box(len(filtered_df))
    with st.container():
        st.markdown('<div class="scroll-box">', unsafe_allow_html=True)
        st.dataframe(filtered_df, use_container_width=True, height=box_height)
        st.markdown('</div>', unsafe_allow_html=True)

    # ----------------------------------------
    # 4️⃣ CRUD Buttons
    # ----------------------------------------
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("➕ Create Course"):
            st.session_state["crud_mode"] = "create"
    with col2:
        if st.button("✏️ Update Course"):
            st.session_state["crud_mode"] = "update"
    with col3:
        if st.button("🗑️ Delete Course"):
            st.session_state["crud_mode"] = "delete"

    crud_mode = st.session_state.get("crud_mode")

    # ----------------------------------------
    # 5️⃣ CRUD FORMS
    # ----------------------------------------
    if crud_mode == "create":
        st.subheader("➕ Create New Course")
        with st.form("create_course_form"):
            title = st.text_input("Course Title")
            description = st.text_area("Description")
            price = st.number_input("Price (€)", min_value=0.0, step=1.0)
            start = st.date_input("Begin Date")
            end = st.date_input("End Date")
            submitted = st.form_submit_button("Create")
            if submitted:
                try:
                    with engine.connect() as conn:
                        conn.execute(text("""
                            CALL new_active_course(:expert_id, :branch_id, :title, :domain, :language, :description, :price, :begin_date, :end_date)
                        """), {
                            "expert_id":  st.session_state.get("selected_expert_id", 121),
                            "branch_id":  1,
                            "title": title,
                            "domain": "inner",
                            "language": "English",
                            "description": description,
                            "price": price,
                            "begin_date": f"{start} 00:00:00",
                            "end_date": f"{end} 00:00:00"
                        })
                        st.success("✅ New course created successfully!")
                except Exception as e:
                    st.error(f"Error creating course: {e}")

    elif crud_mode == "update":
        st.subheader("✏️ Update Existing Course")
        with st.form("update_course_form"):
            course_id = st.number_input("Course ID to Update", step=1)
            new_title = st.text_input("New Title (optional)")
            new_price = st.number_input("New Price", min_value=0.0, step=1.0)
            submitted = st.form_submit_button("Update")
            if submitted:
                try:
                    with engine.connect() as conn:
                        conn.execute(text("""
                            CALL update_course(:course_id, :title, NULL, NULL, :price, NULL, NULL, NULL, NULL, NULL)
                        """), {"course_id": course_id, "title": new_title, "price": new_price})
                        st.success(f"✅ Course ID {course_id} updated successfully!")
                except Exception as e:
                    st.error(f"Error updating course: {e}")

    elif crud_mode == "delete":
        st.subheader("🗑️ Delete Course")
        with st.form("delete_course_form"):
            course_id = st.number_input("Course ID to Delete", step=1)
            submitted = st.form_submit_button("Delete")
            if submitted:
                try:
                    with engine.connect() as conn:
                        conn.execute(text("CALL delete_course(:cid)"), {"cid": course_id})
                        st.warning(f"🗑️ Course ID {course_id} deleted.")
                except Exception as e:
                    st.error(f"Error deleting course: {e}")
