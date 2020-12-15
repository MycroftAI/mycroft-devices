import os, time

os.system("gpio -g mode 16 out")
os.system("gpio -g mode 27 out")
time.sleep(0.1)
os.system("gpio -g write 16 1")
time.sleep(0.1)
os.system("gpio -g write 27 1")
time.sleep(1)
os.system("python /home/mycroft/monkey_patch/send_image_from_rpi.py --direct /home/mycroft/monkey_patch/app_xvf3510_int_spi_boot_v4_1_0.bin")
time.sleep(1)
os.system("i2cdetect -y 1")

"""
from subprocess import Popen, PIPE
import RPi.GPIO as GPIO

def console(cmd):
    p = Popen(cmd, shell=True, stdout=PIPE)
    out, err = p.communicate()
    return (p.returncode, out, err)

XMOS_POWER = 16
XMOS_RESET = 27

# use BCM GPIO pin numbering
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(XMOS_POWER, GPIO.OUT)
GPIO.setup(XMOS_RESET, GPIO.OUT)

time.sleep(0.001)
GPIO.output(XMOS_POWER, 1)
time.sleep(0.001)
GPIO.output(XMOS_RESET, 1)
time.sleep(0.1)

os.system("python /home/mycroft/monkey_patch/send_image_from_rpi.py --direct /home/mycroft/monkey_patch/app_xvf3510_int_spi_boot_v4_1_0.bin")
time.sleep(0.1)
i2c_cmd = "i2cdetect -y 1"
ret_code, out, err = console(i2c_cmd)
time.sleep(0.001)
res = out.decode("utf-8")

if res.find("2c") > -1:
    print("XMOS I2C Device Found")
else:
    print("Error! XMOS I2C Device NOT Found")

#GPIO.cleanup()
"""
