# backend/lay_out.py
import streamlit as st

# def apply_branchlayout():
#     st.markdown("""
#     <style>
#     body {
#         background-color: #ffffff;
#         font-family: 'Inter', sans-serif;
#     }
#     h1, h2, h3, h4 {
#         color: #0a0a0a;
#         font-weight: 700;
#     }
#     p {
#         color: #4b5563;
#     }
#     .section {
#         text-align: center;
#         padding: 3rem 1rem;
#     }
#     .branch-card {
#         background-color: #f9fafb;
#         border-radius: 16px;
#         padding: 2rem;
#         text-align: center;
#         box-shadow: 0 2px 8px rgba(0,0,0,0.05);
#         transition: all 0.3s ease;
#     }
#     .branch-card:hover {
#         transform: translateY(-6px);
#         box-shadow: 0 6px 20px rgba(0,0,0,0.08);
#     }
#     .branch-icon {
#         font-size: 2.5rem;
#         margin-bottom: 10px;
#     }
#     button {
#         border-radius: 8px !important;
#     }
#     </style>
#     """, unsafe_allow_html=True)


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





def apply_layout_footer(): # Custom CSS for clean layout
# -------------------------------------------------
# FOOTER SECTION
# -------------------------------------------------
    st.markdown("<hr>", unsafe_allow_html=True)
    st.markdown("""
    <p style="text-align:center; color:#6b7280; font-size:14px;">
    Made with by <b>Anna Phương & Manisha</b> · Live Library 24/7 · All rights reserved © 2025
    </p>
    """, unsafe_allow_html=True)
