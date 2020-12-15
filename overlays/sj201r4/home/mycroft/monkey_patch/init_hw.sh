
sudo /home/mycroft/monkey_patch/setup_mclk
sudo /home/mycroft/monkey_patch/setup_bclk
sleep 1
sudo insmod /home/mycroft/monkey_patch/i2s_master_loader.ko
arecord -d 1 > /dev/null 2>&1
aplay dummy > /dev/null 2>&1
sleep 1
source /home/mycroft/mycroft-core/venv-activate.sh
python /home/mycroft/monkey_patch/xmosTurnOn.py
python /home/mycroft/monkey_patch/tas5806Test.py
python /home/mycroft/monkey_patch/led_test.py

