# backend/layout_css.py
import streamlit as st


def apply_branchlayout():
    st.markdown("""
    <style>
    body {
        background-color: #ffffff;
        font-family: 'Inter', sans-serif;
        margin-top: 0 !important;
        padding-top: 0 !important;
    }

    h1, h2, h3, h4 {
        color: #0a0a0a;
        font-weight: 700;
        margin-top: 0 !important; #0.1rem
    }

    p {
        color: #4b5563;
    }

    /* Reduce top space before Welcome heading */
    .section {
        text-align: center;
        padding-top: 0 !important;   /* ↓ was 3rem */
        padding-bottom: 1.5rem;
        margin-top: 0 !important;
    }

    # .branch-card {
    #     background-color: #f9fafb;
    #     border-radius: 16px;
    #     padding: 2rem;
    #     text-align: center;
    #     box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    #     transition: all 0.3s ease;
    # }
                
    
      /* 🎨 Equal-size branch cards */
    .branch-card {
        background-color:  #eefdef; #edfdee;#f3f5f7; #f9fafb;
        border-radius: 16px;
        padding: 2rem;
        text-align: center;
        box-shadow: 0 2px 8px rgba(0,0,0,0.05);
        transition: all 0.3s ease;
        
        /* Equal height and alignment */
        min-height: 220px;          /* Ensures uniform height */
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        /* Equal width behavior */
        width: 100%;
        box-sizing: border-box;
    }

    # .branch-card:hover {
    #     transform: translateY(-6px);
    #     box-shadow: 0 6px 20px rgba(0,0,0,0.09);
    # }

    .branch-card:hover {
    transform: translateY(-6px);
    box-shadow: 0 6px 20px rgba(0,0,0,0.09);
    background-color: #83fc8b; #19e526; #b3ffb7;   /* 🌿 light green hover effect */
    }
            

    .branch-icon {
        font-size: 2.5rem;
        margin-bottom: 10px;
    }

    button {
        border-radius: 8px !important;
    }
    </style>
    """, unsafe_allow_html=True)


def apply_layout_scrollable_box(df_length: int):
    """
    Dynamically adjusts the scroll-box height based on number of rows in dataframe.
    - Up to 10 rows → 300px
    - 11–25 rows → 450px
    - 26–50 rows → 600px
    - >50 rows → 800px (max)
    """

    # calculate height dynamically
    if df_length <= 4:
        box_height = 150
    elif df_length <= 25:
        box_height = 250
    elif df_length <= 50:
        box_height = 450
    else:
        box_height = 450

    # render CSS style with dynamic height
    st.markdown(
        f"""
        <style>
        .scroll-box {{
            max-height: {box_height}px;
            overflow-y: auto;
            border: 2px solid #e5e7eb;
            border-radius: 12px;
            padding: 10px;
            background-color: #fafafa;
        }}
        table.dataframe {{
            width: 100%;
            border-collapse: collapse;
        }}
        table.dataframe th, table.dataframe td {{
            text-align: left;
            padding: 8px;
            border-bottom: 1px solid #ddd;
        }}
        table.dataframe th {{
            background-color: #f1f5f9;
            position: sticky;
            top: 0;
            z-index: 2;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )

    return box_height  # optional: return height for debugging or layout logs


# def show_navbar1(go_to):
#     st.markdown(
#         """
#         <style>
#         /* --- NAVBAR STYLING --- */
#         .navbar-container {
#             position: fixed;
#             top: 0;
#             left: 0;
#             right: 0;
#             z-index: 1000;
#             background-color: #ffffff;
#             padding: 0.7rem 2rem;
#             display: flex;
#             justify-content: space-between;
#             align-items: center;
#             border-bottom: 1px solid #eaeaea;
#             box-shadow: 0 1px 5px rgba(0,0,0,0.05);
#         }
#         .nav-title {
#             font-weight: 700;
#             font-size: 1.1rem;
#             color: #111;
#         }
#         .nav-links {
#             display: flex;
#             gap: 1.5rem;
#             align-items: center;
#         }
#         .nav-button {
#             background-color: transparent;
#             border: none;
#             color: #2563eb;
#             font-weight: 600;
#             font-size: 1rem;
#             cursor: pointer;
#         }
#         .nav-button:hover {
#             color: #22c55e;
#         }
#         .login-button > button {
#             background-color: #2563eb !important;
#             color: white !important;
#             font-weight: 600;
#             border-radius: 20px !important;
#             padding: 0.3rem 1rem !important;
#             border: none;
#         }
#         .login-button > button:hover {
#             background-color: #1d4ed8 !important;
#         }
#         .block-container {
#             padding-top: 5rem !important;
#         }
#         </style>
#         """,
#         unsafe_allow_html=True
#     )

#     # --- Streamlit layout buttons ---
#     col1, col2 = st.columns([4, 1])
#     with col1:
#         st.markdown("### 📚 Live Library 24/7")
#     with col2:
#         if st.button("Log in", key="login_nav", help="Access your account"):
#             go_to("login")

def show_navibar():
    st.markdown(
        """ 
        <style>
        /* NAVBAR */
        .navbar {
                    background-color: #f9fafb;
                    padding: 1rem 2rem;
                    border-radius: 12px;
                    margin-bottom: 1.5rem;
                    display: flex;
                    justify-content: space-between;
                    align-items: center;
                    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
                }
        .nav-title {
                    font-weight: 700;
                    color: #19e526;
                    font-size: 1.3rem;
                }
        .nav-links {
                    display: flex;
                    gap: 1.5rem;
                    font-size: 1rem;
                }
        .nav-link {
                    color: #333;
                    text-decoration: none;
                    font-weight: 500;
                }
        .nav-link:hover {
                    color: #19e526;
                    text-decoration: underline;
                }        
        </style> """, 
        unsafe_allow_html=True
)


# =====================================================
# 🌐 NAVBAR FUNCTION
# =====================================================
def show_navbar():
    # --- Detect current page ---
    #query_params = st.experimental_get_query_params()
    #current_page = query_params.get("page", ["home"])[0]

    # --- Navigation bar (with active highlight) ---
    #nav_html = f"""
    st.markdown(
    """
    <style>
    .navbar {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        padding: 0.7rem 1.5rem;
        background-color: #f9f9f9;
        border-radius: 10px;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.05);
        margin-bottom: 1rem;
    }}
    .nav-links {{
        display: flex;
        gap: 1.5rem;
    }}
    .nav-link {{
        font-size: 1rem;
        font-weight: 600;
        text-decoration: none;
        padding: 6px 12px;
        border-radius: 6px;
        transition: all 0.2s ease;
    }}
    .nav-link.active {{
        background-color: #2563eb;
        color: white !important;
    }}
    .nav-link:hover {{
        color: #22c55e;
    }}
    .nav-title {{
        font-size: 1.2rem;
        font-weight: 700;
        color: #111;
    }}
    </style>

    <div class="navbar">
        <div class="nav-title">📚 Live Library 24/7</div>
        <div class="nav-links">
            <a class="nav-link {'active' if current_page == 'home' else ''}" href="/?page=home">🏠 Home</a>
            <a class="nav-link {'active' if current_page in ['analytic','analytics'] else ''}" href="/?page=analytic">📊 Analytic Management</a>
            <a class="nav-link {'active' if current_page in ['admin','administrative'] else ''}" href="/?page=admin">⚙️ Administrative Management</a>
            <a class="nav-link {'active' if current_page == 'chatbot' else ''}" href="/?page=chatbot">💬 Help</a>
        </div>
    </div>
    """
    )
    



def apply_layout_footer(): # Custom CSS for clean layout
#-------------------------------------------------
#FOOTER SECTION
#-------------------------------------------------
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align:center; color:#6b7280; font-size:14px;">
     Live Library 24/7 · All rights reserved © 2025
    </p>
    """, unsafe_allow_html=True)




