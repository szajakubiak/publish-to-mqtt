import passwords
import argparse
import paho.mqtt.client as mqtt
import sys

MQTT_BROKER = passwords.broker
MQTT_PORT = passwords.port
MQTT_USERNAME = passwords.username
MQTT_PASSWORD = passwords.password


def send_mqtt_message(topic, command, debug):
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION1)

    if MQTT_USERNAME and MQTT_PASSWORD:
        client.username_pw_set(MQTT_USERNAME, MQTT_PASSWORD)
        if debug:
            print(f"Username: {MQTT_USERNAME}")
            print(f"Password: {MQTT_PASSWORD}")
    else:
        if debug:
            print("Connecting without username and password")

    try:
        client.connect(MQTT_BROKER, MQTT_PORT, 60)
        client.publish(topic, command, retain=True)
        client.disconnect()
        if debug:
            print(f"Sent {command} to topic {topic}")
    except Exception as e:
        if debug:
            print(f"Failed to send MQTT message: {e}")
        sys.exit(1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MQTT sockets controller")
    parser.add_argument("--topic", "-t", required=True, help="Target topic")
    parser.add_argument(
        "--command",
        "-c",
        choices=["ON", "OFF"],
        required=True,
        help="Command to send (ON or OFF)",
    )
    parser.add_argument(
        "--debug", "-d", required=False, default=False, help="Print debug messages"
    )
    args = parser.parse_args()
    topic = args.topic
    command = args.command
    debug = args.debug
    send_mqtt_message(topic, command, debug)
