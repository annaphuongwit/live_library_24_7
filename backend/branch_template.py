# 3. Versuch mit stored procedures und verbesserter Spaltenbehandlung und rollenabhängiger Ansicht
# backend/branch_template.py
import streamlit as st
from sqlalchemy import text
import pandas as pd
from database import engine
from layout_css import apply_layout_scrollable_box, apply_layout_footer
from live_zoom import show_zoom_by_link
from _auth import logout_button

# ==========================================================
# 🌿 Show Branch Page (e.g., Inner / Health / Social / Finance)
# ==========================================================
def show_branch_by_name(branch_name: str, icon: str, title: str, user: dict | None = None):
    """
    Renders the branch page for the given branch_name.
    Displays all experts and their active courses.
    Also shows user info and logout button at top.
    """
    # Render back to home if clicked Back button
    #go_back_to_home()
    if st.button("⬅️"):
        st.session_state.selected_expert = None
        st.session_state.current_page = "home"
    st.set_page_config(page_title=f"{branch_name.title()} Branch", page_icon=icon, layout="wide")

    # ---------------------------------
    # 1️⃣ Page Header
    # ---------------------------------
    st.markdown(
        f"<h1 style='font-size:2rem; color:#19e526;'>{icon} {title}</h1>",
        unsafe_allow_html=True,
    )

    # ---- User Info + Logout ----
    if user:
        role = (user.get("role") or "").capitalize()
        full_name = user.get("full_name", "Unknown User")
        user_id = user.get("user_id")
        with st.container():
            col1, col2, col3 = st.columns([2, 1, 1])
            with col1:
                st.markdown(
                    f"""
                    <div style='background-color:#f5f5f5; padding:8px 16px; border-radius:10px;'>
                        <strong>👤 {full_name}</strong><br>
                        <span style='font-size:0.5rem; color:gray;'>Role: {role}</span><br>
                        <span style='font-size:0.5rem; color:gray;'>User ID: {user_id}</span>
                    </div>
                    """,
                    unsafe_allow_html=True,
                )
            with col3:
                logout_button()

    # ---------------------------------
    # 2️⃣ Load Branch Data from DB
    # ---------------------------------

    try:
        with engine.connect() as conn:
            query = text("CALL proc_get_experts_and_active_courses_by_branch(:branch_name);")
            experts_df = pd.read_sql(query, conn, params={"branch_name": branch_name})
    except Exception as e:
        st.error(f"Database connection error: {e}")
        st.stop()

    if experts_df.empty:
        st.warning(f"No experts found for the '{branch_name}' branch.")
        return

    experts_df.columns = [c.strip().replace(" ", "_") for c in experts_df.columns]

    # -------------------------------------
    #    LEFT COLUMN — Experts
    # -------------------------------------
    col_left, col_right, col_right_image = st.columns([1.2, 2.5,1.2])
   
    with col_left:
        st.subheader("👩‍🏫 Experts")
        box_height = apply_layout_scrollable_box(len(experts_df))

        # ✅ Ensure unique expert names
        unique_experts = experts_df.drop_duplicates(subset=["Expert_Name"]).reset_index(drop=True)


        # st.markdown('<div class="scroll-box">', unsafe_allow_html=True)
        # st.dataframe(experts_df, use_container_width=True, height=box_height)
        # st.markdown('</div>', unsafe_allow_html=True)

        if "selected_expert" not in st.session_state:
            st.session_state.selected_expert = None

        st.divider()

        # ✅ Show all courses button
        if st.button("📜 Show All Courses", key=f"show_all_{branch_name}"):
            st.session_state.selected_expert = None
            st.rerun()

        # ✅ Expert selection logic
        selected_expert_local = None
        #for idx, expert in experts_df.iterrows():
        for idx, expert in unique_experts.iterrows():
            expert_name = expert.get("Expert_Name", "")
            rating = expert.get("Expert_Rating", "N/A")
            courses = expert.get("Active_Courses", "No active courses")

            key = f"{branch_name}_{expert_name}_{idx}"

            #if st.button(f"⭐ {expert_name}-(Rating:{rating})", key=key):
            if st.button(f"⭐ {expert_name})", key=key):
                selected_expert_local = expert_name

            if st.session_state.selected_expert == expert_name:
                st.markdown(f"**Courses:** {courses}")
                st.markdown("---")

        # ✅ Trigger rerun safely after loop
        if selected_expert_local:
            st.session_state.selected_expert = selected_expert_local
            st.rerun()


# =============================
# RIGHT COLUMN — Courses
# =============================

    with col_right:
        st.subheader("📚 Courses")

        selected_expert = st.session_state.get("selected_expert", None)
        df = pd.DataFrame()

        try:
            with engine.connect() as conn:
                if selected_expert:
                    query = text("""
                        CALL proc_get_courses_by_branch_and_expert(:branch_name, :expert_name);
                    """)
                    df = pd.read_sql(query, conn, params={
                        "branch_name": branch_name,
                        "expert_name": selected_expert.strip()
                    })
                else:
                    query = text("CALL proc_get_active_courses_by_branch(:bname);")
                    df = pd.read_sql(query, conn, params={"bname": branch_name})
        except Exception as e:
            st.error(f"Database error loading courses: {e}")
            st.stop()

        if df.empty:
            st.info(
                f"No active courses found"
                + (f" for **{selected_expert}**" if selected_expert else "")
                + f" in **{branch_name}**."
            )
        else:
            # normalize column names for safe access
            def norm(s: str) -> str:
                return "".join(str(s).lower().replace("_", "").split())
            col_lookup = {norm(c): c for c in df.columns}

            def pick(row, *names, default="—"):
                for n in names:
                    k = norm(n)
                    if k in col_lookup:
                        return row[col_lookup[k]]
                return default

            for _, row in df.iterrows():
                title    = pick(row, "Title", "course_title", default="Untitled Course")
                coach    = pick(row, "Expert_Name", "ExpertName", "Coach", "Coacher", default="Unknown")
                lang     = pick(row, "Language", default="N/A")
                rating   = pick(row, "Rating", "avg_rating", default="N/A")
                price    = pick(row, "Price", default="N/A")
                desc     = pick(row, "Description", default="")
                students = pick(row, "Students", "Total_Students", "TotalStudents", default="—")
                link     = pick(row, "Link", "connect_link", default="")
                begin     = pick(row, "Begin_Date", "begin_date", "Begin", default=None)
                end       = pick(row, "End_Date", "end_date", "End", default=None)

                # Format begin & end dates nicely
                def fmt_date(date_val):
                    if pd.isna(date_val) or not str(date_val).strip():
                        return "—"
                    try:
                        return pd.to_datetime(date_val).strftime("%d %b %Y, %H:%M")
                    except Exception:
                        return str(date_val)

                begin_fmt = fmt_date(begin)
                end_fmt   = fmt_date(end)

                try:
                    rating = f"{float(rating):.1f}"
                except Exception:
                    pass
                #click on link zoom to go to Zoom 
                link_html = (
                    f"<a href='{link}' target='_blank' style='color:#2563eb;'>🔗 Join Live Session on Zoom</a>"
                    if str(link).strip() else ""
                )


                st.markdown(f"""
                <div class="branch-card" style="text-align:left; margin-bottom:1rem;">
                    <h3 style="color:#2563eb; margin-bottom:0.3rem;">{title}</h3>
                    <p><b>Coach:</b> {coach} &nbsp;&nbsp;|&nbsp;&nbsp;
                       <b>Language:</b> {lang} &nbsp;&nbsp;|&nbsp;&nbsp;
                       <b>Rating:</b> ⭐ {rating}</p>
                        <p><b>Begin:</b> {begin_fmt} &nbsp;&nbsp;→&nbsp;&nbsp;
                        <b>End:</b> {end_fmt}</p>
                    <p>{desc}</p>
                    <p><b>Price:</b> €{price} &nbsp;&nbsp; <b>Actuel Students:</b> {students}</p>
                         {link_html} 
                </div>
                """, unsafe_allow_html=True)



# =============================
# RIGHT COLUMN IMAGE— Images Address
# =============================
        selected_expert = st.session_state.get("selected_expert", None)

        # 👉 Only show this column if an expert is selected
        if selected_expert:
            with col_right_image:
                st.subheader("📖 Expert")

                try:
                    with engine.connect() as conn:
                        query = text("""
                            CALL proc_get_expert_contact_by_branch_and_expert(:branch_name, :expert_name);
                        """)
                        prof_df = pd.read_sql(query, conn, params={
                            "branch_name": branch_name,
                            "expert_name": selected_expert.strip()
                        })
                except Exception as e:
                    st.error(f"Database error loading expert info: {e}")
                    prof_df = pd.DataFrame()

                if not prof_df.empty:
                    prof = prof_df.iloc[0]

                    # ✅ If stored Google Drive link, convert to direct link
                    raw_img = str(prof.get("image") or "").strip()
                    img_url = make_direct_image_link(raw_img)

                    email = prof.get("email", "—")
                    address = prof.get("address", "—")
                    telephone = prof.get("telephone", "—")

                    st.image(img_url, width=180, caption=selected_expert)
                    st.markdown(
                        f"""
                        <p><b>📧 Email:</b> {email}</p>
                        <p><b>📍 Address:</b> {address}</p>
                        <p><b>☎️ Telephone:</b> {telephone}</p>
                        """,
                        unsafe_allow_html=True,
                    )
                else:
                    st.info(f"No contact info found for **{selected_expert}**.")
        # 🧩 No expert selected → hide right column entirely
        else:
            pass



            st.markdown(f"""
                <div class="branch-card" style="text-align:left; margin-bottom:1rem;">
                    <h3 style="color:#2563eb; margin-bottom:0.3rem;">{title}</h3>
                    <p><b>Coach:</b> {coach} &nbsp;&nbsp;|&nbsp;&nbsp;
                       <b>Language:</b> {lang} &nbsp;&nbsp;|&nbsp;&nbsp;
                       <b>Rating:</b> ⭐ {rating}</p>
                        <p><b>Begin:</b> {begin_fmt} &nbsp;&nbsp;→&nbsp;&nbsp;
                        <b>End:</b> {end_fmt}</p>
                    <p>{desc}</p>
                    <p><b>Price:</b> €{price} &nbsp;&nbsp; <b>Actuel Students:</b> {students}</p>
                         {link_html} 
                </div>
                """, unsafe_allow_html=True)
            

def make_direct_image_link(url: str) -> str:
    """Return a working, direct-access image URL (Google Drive, static path, or fallback)."""
    if not url or not isinstance(url, str):
        return "https://cdn-icons-png.flaticon.com/512/847/847969.png"

    url = url.strip()

    # 🟢 Case 1 — Google Drive "file/d/.../view" link
    if "drive.google.com" in url:
        try:
            if "/d/" in url:
                file_id = url.split("/d/")[1].split("/")[0]
            elif "id=" in url:
                file_id = url.split("id=")[1].split("&")[0]
            else:
                return "https://cdn-icons-png.flaticon.com/512/847/847969.png"

            # Build a proper direct-view URL
            return f"https://drive.google.com/uc?export=view&id={file_id}"
        except Exception:
            return "https://cdn-icons-png.flaticon.com/512/847/847969.png"

    # 🟢 Case 2 — Local static path
    if url.startswith("/static/"):
        # adjust base URL if your Streamlit runs elsewhere
        return f"http://localhost:8501{url}"

    # 🟢 Case 3 — Already a valid external link (https, png, jpg)
    if url.lower().startswith("http"):
        return url

    # 🟢 Default fallback
    return "https://cdn-icons-png.flaticon.com/512/847/847969.png"



# def make_direct_image_link(url: str) -> str:
#     """Convert Google Drive or other shared links to direct-view image URLs."""
#     if not url or not isinstance(url, str):
#         return "https://cdn-icons-png.flaticon.com/512/847/847969.png"
#     url = url.strip()
#     if "drive.google.com" in url and "/d/" in url:
#         try:
#             file_id = url.split("/d/")[1].split("/")[0]
#             return f"https://drive.google.com/uc?export=view&id={file_id}"
#         except Exception:
#             return "https://cdn-icons-png.flaticon.com/512/847/847969.png"
#     return url

#--------------------------------
# LIVE ZOOM JOIN BUTTON
#--------------------------------
                # # click on link zoom to go to Zoom via Streamlit page switch
                #  # ✅ Replace HTML link with Streamlit navigation
                # if link and str(link).startswith("http"):
                #     if st.button(f"🎥 Join Live Zoom", key=f"join_{title}_{coach}"):
                #         st.session_state["selected_zoom_link"] = link
                #         #st.switch_page("live_zoom.py")
                #         show_zoom_by_link(link)


    st.markdown("---")
    if st.button("⬅️ Back to Home", key=f"back_{branch_name}"):
        # also clear selection when going home
        st.session_state.selected_expert = None
        st.session_state.current_page = "home"

  





