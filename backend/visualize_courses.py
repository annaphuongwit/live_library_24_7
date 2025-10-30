# backend/visualize_courses.py
import streamlit as st
import pandas as pd
from sqlalchemy import text
from database import engine
import matplotlib.pyplot as plt
from layout_css import apply_layout_scrollable_box
#from routers import go_back_to_home


def show_visualize_courses():
    st.set_page_config(page_title="📊 Course Analytics", page_icon="📈", layout="wide")

    #st.title("📊 <span style='color:#19e526'>Live Course Analytics </span>")
    st.markdown("<h1 style='font-size:2.1rem; color:#333;'>📊 <span style='color:#19e526;'>Live Course Analytics</span></h1>", unsafe_allow_html=True)
    st.caption("Visualize course performance, domain distribution, and student reach in real-time.")
    
    # Render back to home if clicked Back button
    #go_back_to_home()
    if st.button("⬅️"):
        st.session_state.selected_expert = None
        st.session_state.current_page = "home"

    # -------------------------------------------------
    # 1️⃣ Load data from MySQL
    # -------------------------------------------------
    try:
        with engine.connect() as conn:
            query = text("SELECT * FROM view_current_courses_status;")
            df = pd.read_sql(query, conn)
    except Exception as e:
        st.error(f"Database connection error: {e}")
        st.stop()

    # -------------------------------------------------
    # 2️⃣ Clean + inspect
    # -------------------------------------------------
    if df.empty:
        st.warning("No course data available in the database.")
        st.stop()

    df.columns = [c.strip().replace(" ", "_") for c in df.columns]

    # Expert name input
    st.markdown("---")
    st.markdown("<h3 style='font-size:1.1rem; color:#333;'><span style='color:#19e526;'>🔍 Search Expert and Visualize Courses</span></h3>", unsafe_allow_html=True)
  
    #st.subheader("🔍 Search Expert and Visualize Courses")

    # -------------------------------------------------
    # 🔍 Expert Filter (case-insensitive & ignores dots)
    # -------------------------------------------------

    expert_list = sorted(df["Expert"].unique().tolist())

    # Text input for live filtering
    expert_input = st.text_input(
        "Enter expert name to filter courses:",
        "",
        key="expert_search_box"
    )

    filtered_df = df  # default: show all
    matched_experts = []

    if expert_input.strip():
        # Normalize input (ignore dots, extra spaces, case)
        def normalize_name(name: str) -> str:
            return name.replace(".", "").strip().lower()

        expert_input_norm = normalize_name(expert_input)

        # Case-insensitive & dot-insensitive partial match
        matched_experts = [
            name for name in expert_list
            if normalize_name(name).startswith(expert_input_norm)
        ]

        if matched_experts:
            st.success(f"✅ Total {len(matched_experts)} expert(s):")
            st.write(", ".join(matched_experts))

            # Case-insensitive & dot-insensitive exact match
            exact_match = [
                name for name in expert_list
                if normalize_name(name) == expert_input_norm
            ]

            if len(exact_match) == 1:
                selected_expert = exact_match[0]
                st.info(f"🔍 Showing analytics for **{selected_expert}**")
                filtered_df = df[df["Expert"].apply(lambda x: normalize_name(x)) == expert_input_norm]
            else:
                # Show combined analytics for all partially matched experts
                matched_norms = [normalize_name(x) for x in matched_experts]
                filtered_df = df[df["Expert"].apply(lambda x: normalize_name(x)).isin(matched_norms)]
        else:
            st.warning("⚠️ No expert name starts with that input. Showing analytics for all experts.")
            filtered_df = df
   
    # -------------------------------------------------
    # 3️⃣ Scrollable Data Table (Dynamic Height)
    # -------------------------------------------------
    df_length = len(filtered_df)

    with st.container():
        # Call the dynamic scroll box function
        box_height = apply_layout_scrollable_box(df_length)

        # Render dataframe inside scroll-box
        st.markdown('<div class="scroll-box">', unsafe_allow_html=True)
        st.dataframe(filtered_df, use_container_width=True, height=box_height)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")

    # -------------------------------------------------
    # 4️⃣ Visualization Grid Layout (3 columns per row)
    # -------------------------------------------------
    df_vis = filtered_df.copy()

    # ---------- 🧭 Row 1: Active vs Inactive ----------
    col1, col2, col3 = st.columns([1.5, 1, 1])
    with col1:
        st.subheader("🧭 Active vs Inactive Courses")
        status_counts = df_vis["current_status"].value_counts()
        fig, ax = plt.subplots()
        ax.pie(status_counts, labels=status_counts.index, autopct="%1.1f%%", startangle=90)
        ax.axis("equal")
        st.pyplot(fig)
    with col2:
        st.markdown("#### Explanation")
        st.write("""
        This chart compares **active courses** with **inactive/upcoming** ones.  
        It helps gauge the engagement level for this expert or overall.
        """)
    with col3:
        total = len(df_vis)
        active = status_counts.get("Active Now", 0)
        inactive = total - active
        st.markdown("#### Description")
        st.metric("Total Courses", total)
        st.metric("Active Now", active)
        st.metric("Inactive/Upcoming", inactive)

    st.markdown("---")

    # ---------- 🧘 Row 2: Courses by Branch ----------
    col1, col2, col3 = st.columns([1.5, 1, 1])
    with col1:
        st.subheader("🧘 Courses by Branch / Domain")
        domain_counts = df_vis["branch_name"].value_counts()
        fig, ax = plt.subplots()
        ax.bar(domain_counts.index, domain_counts.values, color="#2563eb")
        ax.set_xlabel("Branch")
        ax.set_ylabel("Number of Courses")
        ax.set_title("Courses by Branch")
        st.pyplot(fig)
    with col2:
        st.markdown("#### Explanation")
        st.write("""
        This shows how many courses belong to each branch (Inner, Health, Social, Finance).  
        It helps compare domain focus for this expert or overall.
        """)
    with col3:
        st.markdown("#### Description")
        top_branch = domain_counts.idxmax()
        st.metric("Most Courses in Branch", top_branch)
        st.metric("Course Count", domain_counts.max())
        st.metric("Branches Covered", len(domain_counts))

    st.markdown("---")

    # ---------- ⭐ Row 3: Average Course Price ----------
    col1, col2, col3 = st.columns([1.5, 1, 1])
    with col1:
        st.subheader("⭐ Average Course Price per Branch")
        if "price" in df_vis.columns:
            fig, ax = plt.subplots()
            avg_price = df_vis.groupby("branch_name")["price"].mean().sort_values()
            avg_price.plot(kind="bar", ax=ax, color="#f59e0b")
            ax.set_xlabel("Branch")
            ax.set_ylabel("Avg Price (€)")
            st.pyplot(fig)
    with col2:
        st.markdown("#### Explanation")
        st.write("""
        Displays the **average price** of courses for each branch.  
        Shows pricing strategies per domain.
        """)
    with col3:
        st.markdown("#### Description")
        highest = avg_price.idxmax()
        st.metric("Highest-Priced Branch", highest)
        st.metric("Average (€)", round(avg_price.max(), 2))
        st.metric("Overall Mean (€)", round(df_vis["price"].mean(), 2))

    st.markdown("---")

    # ---------- 🎓 Row 4: Total Students per Expert ----------
    col1, col2, col3 = st.columns([1.5, 1, 1])
    with col1:
        st.subheader("🎓 Top Experts by Total Students")
        if "Expert" in df_vis.columns:
            student_by_expert = (
                df_vis.groupby("Expert")["total_students"]
                .sum()
                .sort_values(ascending=False)
            )
            fig, ax = plt.subplots()
            student_by_expert.head(10).plot(kind="barh", ax=ax, color="#10b981")
            ax.set_xlabel("Total Students")
            ax.set_ylabel("Expert")
            st.pyplot(fig)
    with col2:
        st.markdown("#### Explanation")
        st.write("""
        Shows **top experts by total students** (or only the selected expert).  
        Helps identify learner engagement.
        """)
    with col3:
        st.markdown("#### Description")
        top_expert = student_by_expert.index[0]
        st.metric("Most Popular Expert", top_expert)
        st.metric("Total Students", int(student_by_expert.iloc[0]))
        st.metric("Experts Count", len(student_by_expert))

    st.markdown("---")

    # ---------- 💰 Row 5: Course Price Distribution ----------
    col1, col2, col3 = st.columns([1.5, 1, 1])
    with col1:
        st.subheader("💰 Course Price Distribution")
        if "price" in df_vis.columns:
            fig, ax = plt.subplots()
            ax.hist(df_vis["price"], bins=10, color="#2563eb", edgecolor="black")
            ax.set_xlabel("Price (€)")
            ax.set_ylabel("Number of Courses")
            st.pyplot(fig)
    with col2:
        st.markdown("#### Explanation")
        st.write("""
        Shows price distribution (low-cost, mid-range, or premium courses).  
        Useful for pricing analysis per expert or overall.
        """)
    with col3:
        st.markdown("#### Description")
        avg_price = df_vis["price"].mean()
        min_price = df_vis["price"].min()
        max_price = df_vis["price"].max()
        st.metric("Average (€)", round(avg_price, 2))
        st.metric("Lowest (€)", round(min_price, 2))
        st.metric("Highest (€)", round(max_price, 2))

    st.markdown("---")
    #go_back_to_home()
    if st.button("⬅️ Back to Home"):
        st.session_state.selected_expert = None
        st.session_state.current_page = "home"
