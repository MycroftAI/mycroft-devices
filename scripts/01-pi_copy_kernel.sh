#!/bin/sh -x

cd /boot

cp /boot/vmlinuz-* /boot/firmware/kernel8.img.gz
gunzip /boot/firmware/kernel8.img.gz
