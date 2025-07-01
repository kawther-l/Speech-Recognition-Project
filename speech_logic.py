import speech_recognition as sr

def setup_microphone():
    try:
        mic = sr.Microphone()
        return mic
    except OSError:
        return None

def transcribe_speech(mic):
    recognizer = sr.Recognizer()
    
    with mic as source:
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    try:
        return recognizer.recognize_google(audio)
    except sr.UnknownValueError:
        return None
    except sr.RequestError:
        return None
