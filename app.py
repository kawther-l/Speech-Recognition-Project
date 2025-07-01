import streamlit as st
import os
from speech_logic import transcribe_speech

st.set_page_config(page_title="🎙️ Speech Recognition", page_icon="🎤")

st.title("🎙️ Speech-to-Text App")
st.markdown("Speak into your microphone and see your words converted into text.")

# Language selection
language = st.selectbox("🌍 Choose your language", {
    "English (US)": "en-US",
    "French (FR)": "fr-FR",
    "Arabic (TN)": "ar-TN"
})

# API selection
api_choice = st.radio("🧠 Choose Speech Recognition Engine", ("google", "sphinx"))

# Session state for pause/resume
if "paused" not in st.session_state:
    st.session_state.paused = False
if "transcribed_text" not in st.session_state:
    st.session_state.transcribed_text = ""

# Buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🎧 Start Recording"):
        st.session_state.paused = False
        with st.spinner("Recording and transcribing..."):
            result = transcribe_speech(api=api_choice, language=language, pause=False)
            st.session_state.transcribed_text = result
            st.success("✅ Transcription complete!")

with col2:
    if st.button("⏸ Pause"):
        st.session_state.paused = True
        st.info("Recording paused.")

with col3:
    if st.button("💾 Save to File"):
        if st.session_state.transcribed_text:
            with open("transcription.txt", "w", encoding="utf-8") as f:
                f.write(st.session_state.transcribed_text)
            st.success("✅ Transcription saved as `transcription.txt`.")
        else:
            st.warning("⚠️ No transcription to save.")

# Display transcription
if st.session_state.transcribed_text:
    st.markdown("### 📝 Transcribed Text:")
    st.write(st.session_state.transcribed_text)

st.markdown("---")
st.caption("Built with Streamlit & SpeechRecognition")
