from machine import Pin, SoftI2C
from drivers.ds3231 import DS3231
from wrappers.alarm import Alarm

class Clock:
    ds = None
    alarm = Alarm()
    
    def __init__(self, sda, scl):
        self.dt = DS3231(SoftI2C(sda=Pin(sda), scl=Pin(scl)))
        
    def getDateTime(self):
        return self.dt.datetime()
    
    def setDateTime(self, year, month, day, hour, minute, second):
        self.ds.datetime((year, month, day, hour, minute, second))

    def setAlarm(self, hour, minute):
        try:
            self.alarm.set(hour, minute)
            print(f"Alarm is setup for {self.alarm.getHour()}:{self.alarm.getMinute()}")
            self.dt.alarm1((0, self.alarm.getMinute(), self.alarm.getHour()), match=self.dt.AL1_MATCH_HMS)
        except Exception as e:
            print(e)
            
    def getAlarm(self):
        return self.dt.alarm1()
    
    def getStatusAndResetAlarm(self):
        return self.dt.check_alarm(1)
     
#     def resetAlarm(self):
#         return self.dt.check_alarm(2)