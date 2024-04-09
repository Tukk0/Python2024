import datetime
import random

import keywords
import phrase_class as pc
import phrase_variants as pv


# phrase variants: "hello", "welcome back", "good night", "good morning", "good afternoon", "good evening"

time = int(datetime.datetime.now().strftime("%H"))


class Greeting(pc.Phrase):
    def __init__(self):
        super().__init__(pv.Greeting, keywords.Greeting)

    def act(self):
        picker = random.randint(1, 3)
        if picker == 1:
            return self.variants[0]
        if picker == 2:
            return self.variants[1]
        if picker == 3:
            if time < 6:
                return self.variants[2]
            elif time < 12:
                return self.variants[3]
            elif time < 18:
                return self.variants[4]
            else:
                return self.variants[5]

