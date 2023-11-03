from machine import Pin, SoftI2C
import machine
import esp32
from drivers.ds3231 import DS3231
from drivers.ssd1306 import SSD1306_I2C
import time

from arrosoir.arrosoir import Arrosoir
from wrappers.clock import Clock
from wrappers.trigger import Trigger



ARROSOIR_PIN = 19
ALARM_PIN = 15
CLOCK_SDA = 21
CLOCK_SDL = 22
ACTIVATION_TIME = [22, 32]

if __name__ == '__main__':
    print("Initializing ...")
    print("10 seconds to interrupt ...")
    time.sleep(10)
    arrosoir = Arrosoir(ARROSOIR_PIN)
    clock = Clock(CLOCK_SDA, CLOCK_SDL) 
    clock.setAlarm(ACTIVATION_TIME[0],ACTIVATION_TIME[1])
    esp32.wake_on_ext0(pin = Pin(ALARM_PIN, mode = Pin.IN), level = esp32.WAKEUP_ALL_LOW)
    if machine.reset_cause() == machine.DEEPSLEEP_RESET:
        print("Wake up from deep sleep...")
        time.sleep(10)
        print("Arrosing up ....")
        arrosoir.apply(2)
    print("Going to deep sleep...")
    time.sleep(5)
    print("Deep sleep...")
    machine.deepsleep()

#     trigger = Trigger(arrosoir, clock)
#     trigger.setTrigger()
    
    

if __name__ == '_main__':
    print('first test')
    p19 = machine.Pin(19, machine.Pin.OUT)
    while(False):
        p19.on()
        time.sleep(2)
        p19.off()
        time.sleep(2)

if __name__ == '___main__':
    print('first test')
    #arrosoir = Arrosoir()
    #alarm = Alarm(2,0)
    #print(arrosoir.getWakeUpTime())
    #print(alarm.formattedAlarm())
    #i2c = SoftI2C(sda=Pin(21), scl=Pin(22))
    ds = DS3231(SoftI2C(sda=Pin(21), scl=Pin(22)))
    #print(ds.datetime())
    display = SSD1306_I2C(128, 64, SoftI2C(sda=Pin(4), scl=Pin(5)))
    display.fill(0)
    display.text(f'{ds.datetime()[2]}/{ds.datetime()[1]}/{ds.datetime()[0]}',0,0)
    display.text(f'Loading rules...',0,20)
    display.show()
    #ds.alarm1((10), match=ds.AL1_EVERY_S)
    #ds.alarm1((10, 09, 12), match=ds.AL1_MATCH_MS)
    #time.sleep(20)
    #ds.alarm1((40, 09, 12), match=ds.AL1_MATCH_MS)
    #ds.alarm2((15, 00, 12), match=ds.AL1_MATCH_MS)
    #ds.alarm2((31, 11), match=ds.AL2_MATCH_M, weekday=True)
    
#     year = 2023 # Can be yyyy or yy format
#     month = 10
#     mday = 22
#     hour = 2 # 24 hour format only
#     minute = 39
#     second = 0 # Optional
#     weekday = 6 # Optional
# 
#     datetime = (year, month, mday, hour, minute, second, weekday)
#     ds.datetime(datetime)
# 
#     rtc = machine.RTC()
#     rtc.datetime(ds.datetime())
