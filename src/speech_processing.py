import speech_recognition as sr

rec = sr.Recognizer()


def get_message():
    text = "0"
    with sr.Microphone() as source:
        audio = rec.listen(source)
        text = rec.recognize_google(audio, language='en-US')
    return text

