# gotcha_alarm

It's an Arduino/Python project that pretends to have fun and do something useful in the meantime


### Version 1
- Read from two sensors
- Write event logs in a file
- Send email when new event raises

### Version 2
- Web app to see event logs
- Real time system health check

### Version 3
- Recover from internet outage
- Recover from power outage

### Version 4
- Bip alarm
- Voice warning


## Local set-up
- Step into directory
- python3 -m venv gotcha-env
- cd gotcha-env/
- git clone git@github.com:walterbrunetti/gotcha_alarm.git
- cd gotcha_alarm/
- pip install -r requirements.txt
- sudo chmod a+rw /dev/ttyACM0
- set-up configs
- python read_sensor.py
