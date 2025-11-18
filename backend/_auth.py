# backend/_auth.py
import streamlit as st
import hashlib
from sqlalchemy import text
from database import engine


SESSION_KEY = "auth_user"

# ------------------------------------------
# 🔐 Password utilities
# ------------------------------------------
def hash_password(password: str) -> str:
    """Return SHA256 hash of a password (for future upgrades)."""
    return hashlib.sha256(password.encode("utf-8")).hexdigest()

def verify_password(input_password: str, stored_hash: str) -> bool:
    """Support both plaintext demo passwords and hashed ones."""
    if not stored_hash:
        return False
    if len(stored_hash) == 64:  # hashed
        return hash_password(input_password) == stored_hash
    return input_password == stored_hash  # plaintext fallback


# ------------------------------------------
# 🧭 Database query
# ------------------------------------------
def get_user_by_email(email: str):
    """Fetch user record by email."""
    with engine.connect() as conn:
        result = conn.execute(
            text("SELECT user_id, full_name, email, role, language, password_hash FROM users WHERE email = :email"),
            {"email": email.strip()}
        ).mappings().first()
        return dict(result) if result else None


# ------------------------------------------
# 💬 Login UI
# ------------------------------------------
def login_ui():
    # --- Page Title ---
    st.markdown(
        """
        <h2 style='text-align:center; font-weight:700;'>
            🔐 Sign in to <span style="color:#19e526;">Live Library 24/7</span>
        </h2>
        """,
        unsafe_allow_html=True,
    )

    # --- Centered layout using columns ---
    left, center, right = st.columns([1, 2, 1])
    with center:
        st.markdown(
            """
            <style>
            div[data-testid="stForm"] {
                background-color: #ffffff;
                padding: 2.5rem 2rem;
                border-radius: 10px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
                border: 1px solid #e6e6e6;
                max-width: 400px;
                margin: 0 auto;
            }
            div[data-testid="stFormSubmitButton"] button {
                width: 100%;
                border-radius: 6px;
                background-color: #19e526 !important;
                color: #fff !important;
                font-weight: 600;
            }
            div[data-testid="stFormSubmitButton"] button:hover {
                background-color: #16c122 !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        with st.form("login_form", clear_on_submit=False):
            email = st.text_input("Email", placeholder="Enter your email")
            password = st.text_input("Password", type="password", placeholder="Enter your password")
            submitted = st.form_submit_button("Login")

        if submitted:
            user = get_user_by_email(email)
            if not user:
                st.error("❌ Email not found.")
                return False
            if not verify_password(password, user["password_hash"]):
                st.error("⚠️ Incorrect password.")
                return False

            st.session_state[SESSION_KEY] = {
                "user_id": user["user_id"],
                "full_name": user["full_name"],
                "email": user["email"],
                "role": user["role"],
                "language": user["language"],
            }
            st.success(f"✅ Welcome, {user['full_name']}!")
            st.rerun()

        # --- Registration link ---
        st.markdown(
            """
            <div style="text-align:center; margin-top:1rem;">
                <span>Don't have an account?</span>
                <a href="/?page=register" style="color:#2563eb; font-weight:600;">Register here</a>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ------------------------------------------
# ✨ Registration UI (NEW)
# ------------------------------------------
def register_ui():
    st.markdown(
        """
        <h2 style='text-align:center; font-weight:700;'>
            ✨ Create your <span style="color:#19e526;">Live Library 24/7</span> Account
        </h2>
        """,
        unsafe_allow_html=True,
    )

    left, center, right = st.columns([1, 2, 1])
    with center:
        st.markdown(
            """
            <style>
            div[data-testid="stForm"] {
                background-color: #ffffff;
                padding: 2.5rem 2rem;
                border-radius: 10px;
                box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
                border: 1px solid #e6e6e6;
                max-width: 420px;
                margin: 0 auto;
            }
            div[data-testid="stFormSubmitButton"] button {
                width: 100%;
                border-radius: 6px;
                background-color: #2563eb !important;
                color: #fff !important;
                font-weight: 600;
            }
            div[data-testid="stFormSubmitButton"] button:hover {
                background-color: #1d4ed8 !important;
            }
            </style>
            """,
            unsafe_allow_html=True,
        )

        with st.form("register_form", clear_on_submit=False):
            full_name = st.text_input("Full Name", placeholder="Your full name")
            email = st.text_input("Email", placeholder="Enter your email")
            password = st.text_input("Password", type="password", placeholder="Create a password")
            role = st.selectbox("Role", ["Expert", "User"])
            submitted = st.form_submit_button("Create Account")

        if submitted:
            if not full_name or not email or not password:
                st.warning("⚠️ Please fill out all fields.")
                return

            with engine.connect() as conn:
                existing = conn.execute(
                    text("SELECT user_id FROM users WHERE email = :email"), {"email": email}
                ).fetchone()
                if existing:
                    st.error("❌ This email is already registered.")
                    return

                conn.execute(
                    text("""
                        INSERT INTO users (full_name, email, password_hash, role, verified)
                        VALUES (:full_name, :email, :password, :role, 0)
                    """),
                    {
                        "full_name": full_name.strip(),
                        "email": email.strip(),
                        "password": hash_password(password),
                        "role": role.lower(),
                    },
                )
                conn.commit()
                st.success("✅ Account created successfully! You can now log in.")
                st.markdown('<a href="/?page=login" style="color:#2563eb;">Go to Login →</a>', unsafe_allow_html=True)




# def login_ui():
#     # --- Page Title ---
#     st.markdown(
#         """
#         <h2 style='text-align:center; font-weight:700;'>
#             🔐 Sign in to <span style="color:#19e526;">Live Library 24/7</span>
#         </h2>
#         """,
#         unsafe_allow_html=True,
#     )

#     # --- Centered layout using columns ---
#     left, center, right = st.columns([1, 2, 1])
#     with center:
#         st.markdown(
#             """
#             <style>
#             div[data-testid="stForm"] {
#                 background-color: #ffffff;
#                 padding: 2.5rem 2rem;
#                 border-radius: 10px;
#                 box-shadow: 0 4px 20px rgba(0, 0, 0, 0.05);
#                 border: 1px solid #e6e6e6;
#                 max-width: 400px;
#                 margin: 0 auto;
#             }
#             input[type="text"], input[type="password"] {
#                 border: 1px solid #d3d3d3 !important;
#                 border-radius: 6px !important;
#                 padding: 0.6rem !important;
#             }
#             div[data-testid="stFormSubmitButton"] button {
#                 width: 100%;
#                 border-radius: 6px;
#                 background-color: #19e526 !important;
#                 color: #fff !important;
#                 font-weight: 600;
#             }
#             div[data-testid="stFormSubmitButton"] button:hover {
#                 background-color: #16c122 !important;
#             }
#             </style>
#             """,
#             unsafe_allow_html=True,
#         )

#         # --- Login form in the center ---
#         with st.form("login_form", clear_on_submit=False):
#             email = st.text_input("Email", placeholder="Enter your email")
#             password = st.text_input("Password", type="password", placeholder="Enter your password")
#             submitted = st.form_submit_button("Login")

#         if submitted:
#             user = get_user_by_email(email)
#             if not user:
#                 st.error("❌ Email not found.")
#                 return False

#             if not verify_password(password, user["password_hash"]):
#                 st.error("⚠️ Incorrect password.")
#                 return False

#             # ✅ Store session
#             st.session_state[SESSION_KEY] = {
#                 "user_id": user["user_id"],
#                 "full_name": user["full_name"],
#                 "email": user["email"],
#                 "role": user["role"],
#                 "language": user["language"],
#             }
#             st.success(f"✅ Welcome, {user['full_name']}!")
#             st.rerun()




#def login_ui():
    # st.markdown("## 🔐 Sign in to Live Library 24/7")

    # with st.form("login_form"):
    #     email = st.text_input("Email")
    #     password = st.text_input("Password", type="password")
    #     submitted = st.form_submit_button("Login")

    # if submitted:
    #     user = get_user_by_email(email)
    #     if not user:
    #         st.error("❌ Email not found.")
    #         return False

    #     if not verify_password(password, user["password_hash"]):
    #         st.error("⚠️ Incorrect password.")
    #         return False

    #     # ✅ Store user session
    #     st.session_state[SESSION_KEY] = {
    #         "user_id": user["user_id"],
    #         "full_name": user["full_name"],
    #         "email": user["email"],
    #         "role": user["role"],
    #         "language": user["language"],
    #     }
    #     st.success(f"✅ Welcome, {user['full_name']}!")
    #     st.rerun()


# ------------------------------------------
# 🧠 Session management
# ------------------------------------------
def current_user():
    return st.session_state.get(SESSION_KEY)

def require_login():
    """Force login before accessing the app."""
    user = current_user()
    if not user:
        login_ui()
        st.stop()
    return user

def logout_button():
    """Show logout button in top-right corner."""
    user = current_user()
    if user:
        #col1, col2 = st.columns([0.8, 0.2])
        #with col1:
            st.markdown(f"👤 **{user['full_name']}**  |  _{user['role'].capitalize()}_")
        #with col2:
            if st.button("Logout"):
                st.session_state.pop(SESSION_KEY, None)
                st.rerun()
