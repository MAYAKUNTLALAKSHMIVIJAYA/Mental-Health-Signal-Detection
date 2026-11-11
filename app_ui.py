import streamlit as st
from frontends.text_ui import run_text_ui
from frontends.image_ui import run_image_ui
from frontends.audio_ui import run_audio_ui
from frontends.video_ui import run_video_ui

st.set_page_config(
    page_title="Multimodal Mental Health Signal Detection System",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------- Custom CSS (Clean White / Light Theme) ----------
st.markdown("""
<style>
/* Main App Background */
.stApp {
    background-color: #ffffff;
    color: #1e293b;
}

/* Sidebar background */
section[data-testid="stSidebar"] {
    background-color: #f8fafc;
    border-right: 1px solid #e2e8f0;
}

/* Main Title styling */
.main-title {
    font-size: 38px;
    font-weight: 800;
    text-align: center;
    background: linear-gradient(90deg, #0284c7, #2563eb);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 5px;
    letter-spacing: -0.5px;
}

.sub-title {
    font-size: 16px;
    text-align: center;
    color: #64748b;
    margin-bottom: 25px;
}

/* Card Styling */
.card {
    padding: 24px;
    border-radius: 12px;
    background: #ffffff;
    border: 1px solid #e2e8f0;
    box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.03);
    margin-bottom: 20px;
}
</style>
""", unsafe_allow_html=True)

# ---------- Title ----------
st.markdown('<p class="main-title">🧠 Multimodal Emotion & Mental Health Signal Detection</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Analyze emotional signals across Text, Image, Audio, and Video inputs with AI-guided suggestions</p>', unsafe_allow_html=True)

# ---------- Sidebar ----------
st.sidebar.title("🧠 Navigation")
option = st.sidebar.radio(
    "Select Modality",
    ["Text Analysis", "Image Analysis", "Audio Analysis", "Video Analysis"]
)

st.sidebar.markdown("---")
st.sidebar.info("💡 **Mental Health Signal Detection System**\n\nBuilt with Machine Learning & Deep Learning.")
st.sidebar.caption("© 2026 Multimodal Mental Health Signal Detection")

# ---------- Routing ----------
if option == "Text Analysis":
    run_text_ui()

elif option == "Image Analysis":
    run_image_ui()

elif option == "Audio Analysis":
    run_audio_ui()

elif option == "Video Analysis":
    run_video_ui()
