#!/usr/bin/sudo python
# Copyright 2020 Mycroft AI Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from mycroft.enclosure.hardware_enclosure import HardwareEnclosure
from mycroft.enclosure.hardware.Mark2 import Capabilities
import os, sys, time

yellow = (255,255,0)

def bark(caps):
    print("\nUsage: hardware_test board_type")
    print("\n    Where board type is one of ...")
    print([capability for capability in caps.capabilities])
    print("")
    sys.exit(-1)

def dump_capabilities(capabilities):
    for capability in capabilities:
        print("    %s ---> %s" % (capability, capabilities[capability]))

def handle_action():
    print("Received action")

caps = Capabilities()

board_type = None

try:
    board_type = sys.argv[1]
except:
    pass

if board_type not in caps.capabilities and board_type is not None:
    bark(caps)

play_wav_cmd = "aplay ~/mycroft-core/mycroft/res/snd/start_listening.wav"

enclosure_type = "Mark2"

# create enclosure
m2he = HardwareEnclosure(enclosure_type, board_type)

# override action handler so it doesn't
# set a signal
m2he.switches.user_action_handler = handle_action

print("Enclosure Type:%s, Board Type:%s" % (m2he.enclosure_type, m2he.board_type))

print("Enclosure capabilities:")
dump_capabilities(m2he.get_capabilities())

print("\nLed capabilities:")
dump_capabilities(m2he.leds.get_capabilities())

print("\nSwitch capabilities:")
dump_capabilities(m2he.switches.get_capabilities())

print("\nVolume capabilities:")
dump_capabilities(m2he.hardware_volume.get_capabilities())

m2he.leds.fill( (0,0,0) )
m2he.leds._set_led(10,(255,255,0)) # set rsvd yellow
if m2he.switches.SW_MUTE == m2he.switches.active: 
    m2he.leds._set_led(11,(0,255,0)) # set mute yellow
else:
    m2he.leds._set_led(11,(255,0,0)) # set mute yellow

time.sleep(1)

print("set volume to 100%")
m2he.hardware_volume.set_volume(1.0)
os.system(play_wav_cmd)

print("set volume to 20%")
m2he.hardware_volume.set_volume(0.2)
os.system(play_wav_cmd)

print("set volume to 50%")
m2he.hardware_volume.set_volume(0.5)
os.system(play_wav_cmd)

print("fill leds red")
m2he.leds.fill( (255,0,0) )
time.sleep(1)

print("fill leds green")
m2he.leds.fill( (0,255,0) )
time.sleep(1)

print("fill leds blue")
m2he.leds.fill( (0,0,255) )
time.sleep(1)

print("fill leds black")
m2he.leds.fill( (0,0,0) )

print("\n** Push Buttons **")

time.sleep(30)

print("Current volume is %s" % (m2he.hardware_volume.get_hw_volume(),))
os.system(play_wav_cmd)

print("set volume to 40%")
m2he.hardware_volume.set_volume(0.4)
os.system(play_wav_cmd)

print("set volume to 75%")
m2he.hardware_volume.set_volume(0.75)
os.system(play_wav_cmd)

m2he.leds._set_led(10,(0,0,0)) # blank out reserved led
m2he.leds._set_led(11,(0,0,0)) # blank out reserved led

#m2he.terminate()

