# README

## Usage
```shell
$ ./init_hw.sh
```

```shell
$ aplay -l
**** List of PLAYBACK Hardware Devices ****
card 0: sndrpisimplecar [snd_rpi_simple_card], device 0: simple-card_codec_link snd-soc-dummy-dai-0 [simple-card_codec_link snd-soc-dummy-dai-0]
  Subdevices: 1/1
  Subdevice #0: subdevice #0
```

```shell
$ arecord -Dplughw:sndrpisimplecar -f s32 -r 48000 junk.wav
Recording WAVE 'junk.wav' : Signed 32 bit Little Endian, Rate 48000 Hz, Mono
^CAborted by signal Interrupt...
```

```shell
$ aplay junk.wav 
Playing WAVE 'junk.wav' : Signed 32 bit Little Endian, Rate 48000 Hz, Mono
```

```shell
$ ./run_hardware_test.sh
```

##  Manifest
The contents of this directory are as the name suggests, a monkey patch.

They should be moved to more appropriate locations as soon as possible.

- brightness_test.py	- demonstrates softare brightness control
- config.txt		- belongs in /boot/firmware
- hardware_test.py	- what ultimately gets run by run_hardware_test.sh
- i2s_master_loader.ko	- kernel module for i2s xmos support
- init_hw.sh		- run this to set up the hardware 
- led_test.py		- test the leds
- run_hardware_test.sh	- takes in board_type as a cmd line parameter. -h shows all supported board types
- set_ti_vol.py		- 30 is too loud, > 210 is off
- setup_bclk		- provides the bit clock
- setup_mclk		- provides the master clock 
- tas5806Test.py		- initialze the ti amp
- xmosTurnOn.py		- turn on xmos power