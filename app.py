import streamlit as st
import speech_recognition as sr
from speech_logic import transcribe_speech 

# Streamlit page configuration MAIN
st.set_page_config(page_title="Speech-to-Text App", page_icon="🎙️")

# App Title
st.title("🎙️ Real-Time Speech Recognition")
st.markdown("This app records your voice through the microphone and converts it to text using Google Speech Recognition.")

# Main Button For User
if st.button("🎧 Start Recording"):
    st.info("Preparing to record...")
    
    try:
        mic = sr.Microphone()
        with st.spinner("Recording and transcribing..."):
            text = transcribe_speech(mic)
            if text:
                st.success("✅ Transcription complete!")
                st.markdown("**You said:**")
                st.write(text)
    except OSError as e:
        st.error(f"Microphone not found or unavailable: {e}")
    except Exception as e:
        st.error(f"⚠️ An error occurred: {str(e)}")

# Footer 
st.markdown("---")
st.markdown("Made By B&K")
