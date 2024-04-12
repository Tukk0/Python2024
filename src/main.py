import end_session as es
import phrases
import speech_processing as sp

while True:
    text = " " + sp.get_message() + " "
    phrases.checkall(text)
    if es.end_session(text):
        break
    text = "0"

