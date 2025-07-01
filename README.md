# 🎙️ Real-Time Speech Recognition App

This is a simple, browser-based speech-to-text application built using **Streamlit** and **Google's Speech Recognition API**. The app captures audio through the user's microphone and instantly converts spoken words into written text.

---

## 🚀 Features

- 🎧 Real-time voice recording
- 🗣️ Speech-to-text conversion using Google Web Speech API
- 🧠 Automatic ambient noise adjustment
- 🌍 Supports multiple languages and accents
- ✅ Simple, clean user interface built with Streamlit

---

## 🧠 How It Works

The project is split into two main components:

### 1. **Speech Logic (Backend)**
- Sets up the user's microphone.
- Adjusts for ambient noise to improve accuracy.
- Listens to voice input using the `speech_recognition` library.
- Sends audio to Google’s API to get the transcribed text.

### 2. **Streamlit Interface (Frontend)**
- Provides a user-friendly button to start recording.
- Shows status messages like “Listening...” and “Transcribing...”
- Displays the final transcribed text in real time.
- Handles errors like missing microphones or transcription issues.

---

## 🧪 Sample Use Case

> "Hello, this is a speech recognition app that converts my voice into text in real time. I just click the button, speak clearly, and the app shows exactly what I said."

This kind of test helps check how the app handles filler words, casual speaking, or different accents.

---

## 🛠 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/speech-recognition-app.git
cd speech-recognition-app
```

### 2.  Install dependencies

```bash
pip install -r requirements.txt
```

🧾 Requirements
- Python 3.8+
- Microphone
- Internet connection (for Google’s API)

