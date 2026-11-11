import streamlit as st
import os
from backends.audio_backend import predict_audio

def run_audio_ui():

    st.header("🎤 Audio Emotion Detection")

    option = st.radio(
        "Choose Input",
        ["Upload Audio", "Record Audio"]
    )

    os.makedirs("static/temp", exist_ok=True)
    audio_path = None

    if option == "Upload Audio":

        uploaded = st.file_uploader("Upload WAV file", type=["wav"])

        if uploaded:
            audio_path = "static/temp/upload.wav"
            with open(audio_path, "wb") as f:
                f.write(uploaded.read())

            st.audio(audio_path)

    else:
        recorded = st.audio_input("Record voice")

        if recorded:
            audio_path = "static/temp/record.wav"
            with open(audio_path, "wb") as f:
                f.write(recorded.read())

            st.audio(audio_path)

    if audio_path and st.button("🔍 Analyze Audio"):

        with st.spinner("Analyzing voice emotion..."):
            result = predict_audio(audio_path)

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