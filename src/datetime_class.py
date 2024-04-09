import datetime

import phrase_class as pc
import phrase_variants as pv
import keywords

date = datetime.datetime.now().strftime("%d %B, %Y")
time = datetime.datetime.now().strftime("%H:%M %p")


class Date(pc.Phrase):
    def __init__(self):
        super().__init__(pv.Date, keywords.Date)

    def act(self):
        print(date)
        return self.say()


class Time(pc.Phrase):
    def __init__(self):
        super().__init__(pv.Time, keywords.Time)

    def act(self):
        print(time)
        return self.say()

