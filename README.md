# Publish to MQTT
Publish message to the MQTT topic

## Linux setup
* Install Python with virtual environment and git
``` bash
sudo apt install python3 venv git
```

* Create and activate venv
``` bash
python3 -m venv mqttvenv
source mqttvenv/bin/activate
```

* Clone repository
``` bash
git clone https://github.com/szajakubiak/publish-to-mqtt
```

* Install requirements
``` bash
cd publish-to-mqtt/
pip install -r requirements.txt
```

## Usage
After activating the virtual environment can run the script from command line passing the MQTT topic and message as parameters:
``` bash
source mqttvenv/bin/activate
python3 publish.py -t "cmnd/tasmota/POWER" -c "OFF"
```
