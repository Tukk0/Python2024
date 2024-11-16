import speech_recognition as sr

rec = sr.Recognizer()


def get_message():
    try:
        with sr.Microphone() as source:
            audio = rec.listen(source)
            text = rec.recognize_google(audio, language='en-US')
    except sr.UnknownValueError:
        text = "Error"
    return text
