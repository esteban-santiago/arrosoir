import os
import time
from machine import Pin

class Arrosoir:
    controller = 0
    
    def __init__(self, controller):
        self.controller = controller
        
    def setController(self, pin):
        self.controller = pin
    
    def getController(self):
        return self.controller
    
    def getWakeUpTime(self):
        return self.wakeUpTime.split(':')
    
    def start(self):
        try:
            Pin(self.controller, Pin.OUT).on()
            return True
        except Exception as e:
            print(e)
            return False
        
    def stop(self):
        try:
            Pin(self.controller, Pin.OUT).off()
            return True
        except Exception as e:
            print(e)
            return False
     
    def apply(self, seconds):
        self.start()
        time.sleep(seconds)
        self.stop()
