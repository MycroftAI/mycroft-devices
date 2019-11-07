#!/bin/sh -x

cd /boot

cp /boot/Image.gz-* /boot/firmware/kernel8.img.gz
gunzip /boot/firmware/kernel8.img.gz
