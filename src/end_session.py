import keywords


def end_session(text):
    for keyword in keywords.Farewell:
        if keyword in text:
            return True

