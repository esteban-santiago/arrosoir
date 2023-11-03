import network
import ubinascii

class EspNow:
    def __init__(self):
        pass
        
    def getMacAddress(self):
        return ubinascii.hexlify(network.WLAN(network.STA_IF).config('mac'))
    
    def getMacAddressStr(self):
        return self.getMacAddress().decode()
    
    def sendMsg(self, message):
        pass
    
    def receiveMsg(self):
        pass
