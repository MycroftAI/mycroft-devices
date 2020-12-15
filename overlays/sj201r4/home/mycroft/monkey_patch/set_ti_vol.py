'''
install:
    pip3 install smbus2

run:
    python3 set_ti_vol.py vol
    where vol is > 30 and < 210
'''
from smbus2 import SMBus
import os, sys, time
import subprocess

class tasThing:
    devAddr = 0x2f
    bus = ""

    commandReturn = ""
    
    def __init__(self):
        self.bus = SMBus(1)
        
    def writeData(self, addr, val, comment = "" ):
        self.bus.write_byte_data(self.devAddr, addr , val)
        print("write: %s: %s - %s" %(hex(addr),hex(val), comment ) )
        time.sleep(0.1)
    
    def close(self):
        self.bus.close()
    
    def setVolume(self, vol):
        if vol < 30:
            vol = 30

        if vol > 210:
            vol = 210

        setVolStr = "Set Volume %s" %( str (vol) )
        self.writeData(0x4c,vol ,setVolStr) #Set volume

if __name__ == '__main__':
    vol = int( sys.argv[1] )
    tt = tasThing()
    tt.setVolume(vol)
    tt.close()
    time.sleep(1)
    os.system("aplay /home/mycroft/mycroft-core/mycroft/res/snd/start_listening.wav")
