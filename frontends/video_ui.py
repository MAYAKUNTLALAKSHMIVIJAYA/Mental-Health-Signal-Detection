import streamlit as st
import tempfile
from backends.video_backend import predict_video
from utils.live_video_recorder import record_live_video

def run_video_ui():

    st.header("🎥 Video Emotion Detection")

    option = st.radio(
        "Choose Input",
        ["Upload Video", "Record Live Video"]
    )

    video_path = None

    if option == "Upload Video":

        uploaded = st.file_uploader("Upload video", type=["mp4","avi","mov"])

        if uploaded:
            temp = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
            temp.write(uploaded.read())
            video_path = temp.name
            st.video(video_path)

    else:
        st.warning("Recording will capture 5 seconds")

        if st.button("🎬 Start Recording"):
            video_path = record_live_video(duration=5)
            st.success("Recording completed")
            st.video(video_path)

    if video_path and st.button("🔍 Analyze Video"):

        with st.spinner("Analyzing video emotion..."):
            result = predict_video(video_path)

        st.success(f"{result['prediction']} ({result['confidence']:.2f})")

        st.subheader("📊 Emotion Distribution")
        st.image(result["histogram_path"])

        st.subheader("💡 Suggestions")
        sug = result["suggestions"]

        st.subheader("🎬 Recommended Movies")
        st.info(", ".join(sug["movies"]))

        st.subheader("🎵 Recommended Songs")
        st.success(", ".join(sug["songs"]))

        st.subheader("📜 Recommended Poems")
        st.warning(", ".join(sug["poems"]))

        st.subheader("💡 Motivation for You")
        for m in sug["motivation"]:
            st.write("•", m)