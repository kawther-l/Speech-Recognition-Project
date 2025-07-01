import speech_recognition as sr

def transcribe_speech(api="google", language="en-US", pause=False):
    recognizer = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            if pause:
                return None
            audio = recognizer.listen(source, timeout=None, phrase_time_limit=20)

        if api == "google":
            return recognizer.recognize_google(audio, language=language)
        elif api == "sphinx":
            return recognizer.recognize_sphinx(audio)

        else:
            return "Unsupported API selected."

    except sr.UnknownValueError:
        return "⚠️ Sorry, I couldn’t understand what you said."
    except sr.RequestError as e:
        return f"⚠️ Could not request results from the service: {e}"
    except OSError as e:
        return f"⚠️ Microphone error: {e}"
    except Exception as e:
        return f"⚠️ Unexpected error: {e}"
