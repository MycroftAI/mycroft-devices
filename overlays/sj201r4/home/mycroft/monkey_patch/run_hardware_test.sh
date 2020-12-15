#!/bin/bash
#
# usage - run_hardware_test.sh board_type
#
# for a list od supported board types run
# ./run_hardware_test.sh -h 

# Enter the Mycroft venv
source "/home/mycroft/mycroft-core/venv-activate.sh" -q

python /home/mycroft/test/hardware_test.py $1
