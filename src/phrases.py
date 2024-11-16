import keywords
import playsound

import links
from datetime_class import Date, Time
from greeting_class import Greeting
from phrase_class import Phrase
import phrase_variants as pv

Greeting = Greeting()
Time = Time()
Date = Date()
Farewell = Phrase(pv.Farewell, keywords.Farewell)
Google = Phrase(pv.Google, keywords.Google, is_a_link=True, link=links.google_link)
Youtube = Phrase(pv.Youtube, keywords.Youtube, is_a_link=True, link=links.youtube_link)
Mipt = Phrase(pv.Mipt, keywords.Mipt, is_a_link=True, link=links.mipt_link)
Github = Phrase(pv.Github, keywords.Github, is_a_link=True, link=links.github_link)
phrases = [Greeting, Farewell, Time, Date, Google, Youtube, Mipt, Github]


def checkall(text):
    for phrase in phrases:
        if phrase.check(text):
            sound = phrase.act()
            playsound.playsound(sound)
            break
    else:
        print("Sorry, I don't understand you")

