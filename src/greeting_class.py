import datetime
import random

import keywords
import phrase_class as pc
import phrase_variants as pv
import time_aliases as ta

# phrase variants: "hello", "welcome back", "good night", "good morning", "good afternoon", "good evening"


class Greeting(pc.Phrase):
    def __init__(self):
        super().__init__(pv.Greeting, keywords.Greeting)

    def act(self):
        picker = random.randint(1, 3)
        if picker == ta.hello_variant:
            return self.variants[0]
        if picker == ta.welcome_back_variant:
            return self.variants[1]
        if picker == ta.time_of_day_variant:
            time = int(datetime.datetime.now().strftime("%H"))
            if time < ta.morning_hours:
                return self.variants[2]
            elif time < ta.afternoon_hours:
                return self.variants[3]
            elif time < ta.evening_hours:
                return self.variants[4]
            else:
                return self.variants[5]
