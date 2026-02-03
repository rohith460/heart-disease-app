import streamlit as st
from database import create_user_table
from auth import login_user, register_user

# -------------------------
# Hide Streamlit sidebar
# -------------------------
st.markdown("""
<style>
[data-testid="stSidebar"] {
    display: none;
}
[data-testid="collapsedControl"] {
    display: none;
}
</style>
""", unsafe_allow_html=True)

# Initialize DB
create_user_table()

st.set_page_config(
    page_title="AI-Powered Heart Disease Risk System",
    layout="wide"
)

# -------------------------
# Session state
# -------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "current_page" not in st.session_state:
    st.session_state.current_page = "login"

if "show_profile" not in st.session_state:
    st.session_state.show_profile = False

# =========================
# LOGIN / REGISTER PAGE
# =========================
if not st.session_state.logged_in:

    st.markdown("""
    <style>
    /* ===== Input box visibility ===== */
    input {
        background-color: #ffffff !important;
        border: 2px solid #1a4a7a !important;
        border-radius: 8px !important;
        color: #102a43 !important;
    }
    /* Profile popover box */
    div[data-testid="stPopover"] {
        border: 2px solid #1a4a7a !important;
        border-radius: 12px !important;
        box-shadow: 0 12px 30px rgba(0,0,0,0.25) !important;
        background-color: #ffffff !important;
    }

    /* Popover text */
    div[data-testid="stPopover"] * {
        color: #102a43 !important;
    }

    /* Profile button styling */
    button:has(span:contains("👤")) {
        background-color: #2563eb !important;
        color: #ffffff !important;
        border-radius: 50px !important;
        padding: 6px 14px !important;
    }

    /* Hover */
    button:has(span:contains("👤")):hover {
        background-color: #1d4ed8 !important;
    }

    /* Password eye icon visibility */
    button[title="Show password"] svg {
        color: #1a4a7a !important;
    }

    [data-testid="stAppViewContainer"] {
        background:
          linear-gradient(rgba(10,25,47,0.85), rgba(10,25,47,0.85)),
          url("https://images.unsplash.com/photo-1588776814546-1ffcf47267a5");
        background-size: cover;
        background-position: center;
    }

    .block-container {
        max-width: 420px;
        margin-top: 12vh;
        background: rgba(255,255,255,0.96);
        padding: 2.5rem;
        border-radius: 18px;
        box-shadow: 0 20px 45px rgba(0,0,0,0.45);
    }

    h1, h2, h3, label {
        color: #1a4a7a !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.markdown("## 🔐 Login / Register")

    tab1, tab2 = st.tabs(["Login", "Register"])

    with tab1:
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Login"):
            user = login_user(username, password)
            if user:
                st.session_state.logged_in = True
                st.session_state.username = username
                st.session_state.current_page = "awareness"
                st.rerun()
            else:
                st.error("Invalid username or password")

    with tab2:
        new_user = st.text_input("New Username")
        new_pass = st.text_input("New Password", type="password")

        if st.button("Register"):
            if register_user(new_user, new_pass):
                st.success("Registration successful. Please login.")
            else:
                st.error("Username already exists")

# =========================
# AFTER LOGIN (THIS WAS MISSING)
# =========================
else:
    st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background:
        linear-gradient(rgba(10,25,47,0.85), rgba(10,25,47,0.85)),
        url("https://images.unsplash.com/photo-1588776814546-1ffcf47267a5");
        background-size: cover;
        background-attachment: fixed;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
    <style>
    [data-testid="stMarkdownContainer"] h1,
    [data-testid="stMarkdownContainer"] h2,
    [data-testid="stMarkdownContainer"] h3,
    [data-testid="stMarkdownContainer"] p,
    [data-testid="stMarkdownContainer"] li,
    strong {
        color: #f1f5f9 !important;
    }
    </style>
    """, unsafe_allow_html=True)
    # =========================
    # TOP BAR (STABLE VERSION)
    # =========================
    top_spacer, top_profile, top_logout = st.columns([8, 2, 2])

    with top_profile:
        if st.button("👤 Profile", key="profile_toggle"):
            st.session_state.show_profile = not st.session_state.show_profile

    with top_logout:
        if st.button("🚪 Logout"):
            st.session_state.logged_in = False
            st.session_state.current_page = "login"
            st.rerun()
    if st.session_state.show_profile:
        st.markdown(
        f"""
        <div style="
        position: fixed;
        top: 85px;
        right: 24px;
        width: 280px;
        background: linear-gradient(135deg, #1a4a7a, #2563eb);
        border-radius: 16px;
        padding: 18px;
        box-shadow: 0 18px 45px rgba(0,0,0,0.45);
        z-index: 9999;
        font-family: 'Segoe UI', sans-serif;
        color: white;
        ">

        <div style="display:flex; align-items:center; gap:10px; margin-bottom:12px;">
        <span style="font-size:26px;">👤</span>
        <h3 style="margin:0;">User Profile</h3>
        </div>

        <p><b>Username:</b> {st.session_state.get("username", "User")}</p>
        <p><b>Status:</b> Logged in</p>
        <p><b>Role:</b> User</p>

        <hr style="border:1px solid rgba(255,255,255,0.35); margin:12px 0;">

        <p style="font-size:12px; opacity:0.85;">
        AI-Powered Heart Disease Risk System
        </p>

        </div>
        """,
        unsafe_allow_html=True
        )




    # ---- Page routing ----
    if st.session_state.current_page == "awareness":
        import pages.awareness as awareness
        awareness.show()

    elif st.session_state.current_page == "predict":
        import pages.predict as predict
        predict.show()
    