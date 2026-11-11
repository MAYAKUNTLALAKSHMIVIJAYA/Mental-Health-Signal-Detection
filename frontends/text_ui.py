import streamlit as st
from backends.text_backend import predict_text

def run_text_ui():

    st.header("📝 Text Emotion Analyzer")
    st.write("Enter your thoughts and AI will detect emotional state")

    user_text = st.text_area("Type your text here", height=150)

    col1, col2 = st.columns([1,1])

    with col1:
        analyze = st.button("🔍 Analyze Emotion", use_container_width=True)

    if analyze:

        if user_text.strip() == "":
            st.warning("Please enter some text")
            return

        with st.spinner("Analyzing emotions..."):
            result = predict_text(user_text)

        st.success(f"Detected Emotion: {result['prediction']} ({result['confidence']:.2f})")

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