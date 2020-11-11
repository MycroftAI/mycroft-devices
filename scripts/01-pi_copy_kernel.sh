#!/bin/sh -x

cd /boot

if [ $1 = "armhf" ]; then
    cp /boot/vmlinuz-* /boot/firmware/kernel.img
else
    cp /boot/vmlinuz-* /boot/firmware/kernel8.img.gz
    gunzip /boot/firmware/kernel8.img.gz
fi
