import utime as time

"""
    (2023, 10, 22, 0, 33, 55, 6, 295)
    year includes the century (for example 2014).
    month is 1-12
    mday is 1-31
    hour is 0-23
    minute is 0-59
    second is 0-59
    weekday is 0-6 for Mon-Sun
    yearday is 1-366

"""

class Alarm:
    hour = 20
    minute = 0
    
    def __init__(self):
        pass
    
    def set(self, hour, minute):
        try:
            self.hour = hour
            self.minute = minute
        except Exception as e:
            print(e)
    
    def getHour(self):
        return self.hour
    
    def getMinute(self):
        return self.minute

