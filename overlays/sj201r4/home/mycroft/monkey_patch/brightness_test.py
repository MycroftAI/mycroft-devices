from mycroft.enclosure.hardware.MycroftLed.led_sj201r4 import Led
import time

pel = 7

l = Led()

while True:
    for brightness in range(0, 255, 10):
        #color = (brightness, 0, 0)  # red
        color = (0, brightness, 0)  # green
        l.set_led(pel, color)
        time.sleep(0.05)

    for brightness in range(255, 0, -10):
        #color = (brightness, 0, 0)  # red
        color = (0, brightness, 0)  # green
        l.set_led(pel, color)
        time.sleep(0.05)
