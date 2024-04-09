import keywords
import phrases
import speech_processing as sp

while True:
    text = sp.get_message()
    phrases.checkall(text)
    for keyword in keywords.Farewell:
        if keyword in text:
            break

