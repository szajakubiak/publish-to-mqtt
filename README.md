# Publish to MQTT
Publish message to the MQTT topic

## Linux setup
* Install Python with virtual environment and git
``` bash
sudo apt install python3 venv git
```

* Create and activate venv
``` bash
cd ~
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

You can use cron to automate control of your device. Run the cron editor:
``` bash
crontab -e
```

If you run the editor for the first time you need to choose the default text editor. If you don't have any preferred editor select **nano**. Then scroll all the way down in the file. Here you can add a line to automate your device. As an example let's add a line which will send the command **OFF** to the device each day at 23:00:
``` bash
0 23 * * * ~/mqttvenv/bin/python3 ~/publish-to-mqtt/publish.py -t "cmnd/tasmota/POWER" -c "OFF"
```

If you use **nano* as a text editor press Ctrl+o to save and Ctrl+x to exit.

You can use [this site](https://crontab.guru/) to learn how to create cron schedules. Note that we used a direct link to the Python 3 binary file inside the virtual environment. This way we can run the script without activating the venv.
