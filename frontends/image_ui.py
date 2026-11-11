import streamlit as st
import numpy as np
import cv2
from backends.image_backend import predict_image

def run_image_ui():

    st.header("📷 Image Emotion Detection")

    option = st.radio(
        "Choose Input Method",
        ["Upload Image", "Capture From Camera"]
    )

    image = None

    if option == "Upload Image":
        uploaded = st.file_uploader("Upload image", type=["jpg","png","jpeg"])

        if uploaded:
            file_bytes = np.asarray(bytearray(uploaded.read()), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, 1)

    else:
        captured = st.camera_input("Capture image")

        if captured:
            file_bytes = np.asarray(bytearray(captured.read()), dtype=np.uint8)
            image = cv2.imdecode(file_bytes, 1)

    if image is not None:
        st.image(image, channels="BGR", caption="Input Image")

        if st.button("🔍 Analyze Image"):
            with st.spinner("Analyzing facial emotion..."):
                result = predict_image(image)

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