#!/bin/sh

# Create SPI group and add mycroft user to it
groupadd spi
usermod -a -G spi mycroft
chown root.spi /dev/spidev*
chmod g+rw /dev/spidev*