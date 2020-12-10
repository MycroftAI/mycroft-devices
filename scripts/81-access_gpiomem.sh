#!/bin/sh

# Create GPIO group and add mycroft user to it
groupadd gpio
usermod -a -G gpio mycroft
chown root.gpio /dev/gpiomem
chmod g+rw /dev/gpiomem