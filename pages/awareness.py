import streamlit as st
import matplotlib.pyplot as plt
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
/* Force text visibility on dark background */
h1, h2, h3, h4, h5, h6, p, li, span, div {
    color: #f1f5f9 !important;
}

/* Button text */
button {
    color: #ffffff !important;
}

/* Subheader color */
[data-testid="stMarkdownContainer"] h2 {
    color: #cfe8ff !important;
}
</style>
""", unsafe_allow_html=True)

def show():
    st.markdown("""
    <style>
    button[kind="secondary"] {
        background-color: #1a4a7a !important;
        color: white !important;
        border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🫀 Heart Disease Awareness")

    st.markdown("""
    Heart disease is one of the **leading causes of death worldwide**.
    Awareness and early prediction can save lives.
    """)

    st.subheader("❤️ Common Types of Heart Disease")
    st.markdown("""
    - Coronary artery disease  
    - Heart attack  
    - Arrhythmia  
    - Heart failure  
    """)

    # ==============================
    # Awareness Visualization
    # ==============================

    st.markdown("## 📊 Global Heart Disease Overview")

    labels = [
        "Heart Disease",
        "Stroke",
        "Other Causes"
    ]

    sizes = [32, 27, 41]

    colors = ["#e63946", "#457b9d", "#a8dadc"]

    # ---- Smaller figure ----
    fig1, ax = plt.subplots(figsize=(4.2, 4.2))
    fig1.patch.set_facecolor("#f5f9ff")  # soft light background

    ax.pie(
        sizes,
        labels=labels,
        autopct="%1.1f%%",
        startangle=140,
        colors=colors,
        pctdistance=0.75,   # % text closer to center
        labeldistance=1.12, # labels outside & clear
        textprops={
            "color": "#102a43",
            "fontsize": 11,
            "weight": "bold"
        },
        wedgeprops={
            "linewidth": 1.2,
            "edgecolor": "white"
        }
    )

    ax.set_title(
        "Global Cardiovascular Death Distribution",
        fontsize=12,
        color="#1a4a7a",
        pad=12
    )

    ax.axis("equal")

    # ==============================
    # Layout: LEFT (Chart) | RIGHT (Summary)
    # ==============================

    col_left, col_right = st.columns([1.1, 1.6])

    with col_left:
        st.pyplot(fig1)

    with col_right:
        st.markdown("""
        ### 🧠 Key Insights
        - **Heart disease** remains the **leading global cause of death**
        - A large percentage of cases are **preventable**
        - Early detection dramatically improves survival rates

        ### 📌 Why this matters
        Awareness helps individuals:
        - Monitor risk factors early  
        - Adopt healthier lifestyles  
        - Reduce long-term complications  

        👉 Use prediction tools to **act before symptoms appear**.
        """)



    st.subheader("✅ Good Heart Health Practices")
    st.markdown("""
    - Regular exercise  
    - Healthy diet  
    - Avoid smoking  
    - Control BP & cholesterol  
    """)

    st.markdown("---")
    col1, col2 = st.columns(2)

    with col1:
        if st.button("🔍 Predict Your Risk"):
            st.session_state.current_page = "predict"
            st.rerun()

