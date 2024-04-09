import random
from time import sleep

import links_processing as lp


class Phrase:
    def __init__(self, variants, keywords, is_a_link=False, link=""):
        self.variants = variants
        self.keywords = keywords
        self.is_a_link = is_a_link
        self.link = link

    def say(self):
        return random.choice(self.variants)

    def say_with_pause(self, pause):
        sleep(pause)
        return self.say()

    def act(self):
        if self.is_a_link:
            lp.open_link(self.link)
        return self.say()

    def check(self, text):
        for keyword in self.keywords:
            if keyword in text:
                return True
        return False

