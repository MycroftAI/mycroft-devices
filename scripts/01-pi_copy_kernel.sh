#!/bin/sh -x

cd /boot
ls -l
gunzip Image.gz
cp Image /boot/firmware/kernel8.bin
