# backend/live_zoom.py
import streamlit as st
from sqlalchemy import create_engine, text

# =====================================================
# 🎥 Live Zoom Integration for Live Library 24/7
# =====================================================
def show_zoom_by_link(zoom_url: str):
    # """Embed Zoom meeting in Streamlit page given a Zoom URL."""
    # zoom_url = zoom_url.strip()
    # # Ensure browser join parameter
    # if "?browser=1" not in zoom_url:
    #     zoom_url = zoom_url + ("&browser=1" if "?" in zoom_url else "?browser=1")

    # st.markdown("---")
    # st.subheader("🔗 Embedded Live Session")
    # st.markdown("<p style='color:gray;'>If you cannot see the Zoom window below, click “Open in new tab”.</p>", unsafe_allow_html=True)

    # # --- Embed Zoom iframe
    # st.markdown(f"""
    # <iframe src="{zoom_url}"
    #         width="100%"
    #         height="620"
    #         style="border:1px solid #ccc;border-radius:10px;"
    #         allow="camera; microphone; fullscreen; display-capture"
    #         frameborder="0"
    #         id="zoomFrame"
    #         onerror="document.getElementById('zoomFallback').style.display='block';">
    # </iframe>

    # <div id="zoomFallback" style="display:none;margin-top:20px;padding:20px;border:1px solid #ff9999;border-radius:10px;background-color:#fff6f6;">
    #     <h4>⚠️ Zoom cannot load inside this browser.</h4>
    #     <p>Please <a href="{zoom_url}" target="_blank" style="color:#19e526;font-weight:bold;">open this Zoom meeting in a new tab</a> instead.</p>
    # </div>

    # <script>
    #     setTimeout(function() {{
    #         var iframe = document.getElementById('zoomFrame');
    #         if (!iframe || iframe.contentWindow.location.href === 'about:blank') {{
    #             document.getElementById('zoomFallback').style.display = 'block';
    #         }}
    #     }}, 5000);
    # </script>
    # """, unsafe_allow_html=True)


# # --- Database connection (consistent with database.py)
# engine = create_engine("mysql+pymysql://root:Sonne1!#@localhost:3306/live_library_manage_system")

# # --- Page setup
# st.set_page_config(page_title="🎥 Live Zoom Session", layout="wide")
# st.markdown("<h1 style='color:#19e526;'>🎥 Live Zoom Sessions</h1>", unsafe_allow_html=True)
# st.caption("Join your live session directly in the browser or open in Zoom app if embedding is not supported.")

# # --- Fetch all active courses with Zoom links
# with engine.connect() as conn:
#     result = conn.execute(text("""
#         SELECT course_id, title, connect_link, domain, language, begin_date
#         FROM courses
#         WHERE is_active = 1 AND connect_link IS NOT NULL
#         ORDER BY begin_date ASC
#     """))
#     courses = result.fetchall()

# if not courses:
#     st.info("⚠️ No active live Zoom sessions available right now.")
# else:
#     # --- Display in table format for overview
#     st.markdown("### 📅 Upcoming Live Sessions")
#     for c in courses:
#         with st.expander(f"{c.title}  —  ({c.domain.title()}) [{c.language}]"):
#             st.write(f"🗓️ **Start Time:** {c.begin_date}")
#             st.write(f"🌐 **Zoom Link:** {c.connect_link}")
#             join_key = f"join_{c.course_id}"
#             if st.button("▶️ Join Now", key=join_key):
#                 st.session_state["selected_zoom_link"] = c.connect_link

#     # --- If a Zoom link is selected
#     if "selected_zoom_link" in st.session_state:
#         zoom_url = st.session_state["selected_zoom_link"].strip()


        zoom_url = zoom_url.strip()

        # Ensure browser join parameter
        if "?browser=1" not in zoom_url:
            zoom_url = zoom_url + ("&browser=1" if "?" in zoom_url else "?browser=1")

        st.markdown("---")
        st.subheader("🔗 Embedded Live Session")
        st.markdown("<p style='color:gray;'>If you cannot see the Zoom window below, click “Open in new tab”.</p>", unsafe_allow_html=True)

        # --- Embed Zoom iframe
        st.markdown(f"""
        <iframe src="{zoom_url}"
                width="100%"
                height="620"
                style="border:1px solid #ccc;border-radius:10px;"
                allow="camera; microphone; fullscreen; display-capture"
                frameborder="0"
                id="zoomFrame"
                onerror="document.getElementById('zoomFallback').style.display='block';">
        </iframe>

        <div id="zoomFallback" style="display:none;margin-top:20px;padding:20px;border:1px solid #ff9999;border-radius:10px;background-color:#fff6f6;">
            <h4>⚠️ Zoom cannot load inside this browser.</h4>
            <p>Please <a href="{zoom_url}" target="_blank" style="color:#19e526;font-weight:bold;">open this Zoom meeting in a new tab</a> instead.</p>
        </div>

        <script>
            setTimeout(function() {{
                var iframe = document.getElementById('zoomFrame');
                if (!iframe || iframe.contentWindow.location.href === 'about:blank') {{
                    document.getElementById('zoomFallback').style.display = 'block';
                }}
            }}, 5000);
        </script>
        """, unsafe_allow_html=True)
