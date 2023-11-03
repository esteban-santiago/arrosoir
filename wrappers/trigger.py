from machine import Pin
from time import sleep
from arrosoir import *
from wrappers import *


class Trigger:
    arrosoir = None
    alarm = None
    pin = None
    
    def __init__(self, arrosoir, clock):
        self.arrosoir = arrosoir
        self.clock = clock
        
    def setTrigger(self):
        try:
            self.pin = Pin(23, Pin.IN)
            self.pin.irq(trigger=Pin.IRQ_FALLING, handler=self.executeAction)
            print("Trigger seted up")
        except Exception as e:
            print(e)
    
    
    def executeAction(self, callback):
        print(f"Invoke executeAction: {callback}")
        self.arrosoir.start()
        sleep(1) #Une segonde
        self.arrosoir.stop()
        self.clock.resetAlarm()
        