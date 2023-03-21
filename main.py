import time

from paho.mqtt import client as mqtt_client
import random

# I used a free public broker
broker = 'broker.emqx.io'
port = 1883
topic_state = 'smart-light-bulb/state'
topic_brightness = 'smart-light-bulb/brightness'

client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'


def connect_mqtt():
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client):
    msg_count = 0
    while True:
        #send state
        msg = random.randint(0, 1)
        result = client.publish(topic_state, msg)
        status = result[0]
        #send brightness
        time.sleep(3)
        msg1 = random.randint(0, 100)
        result1 = client.publish(topic_brightness, msg1)
        status1 = result1[0]
        if status == 0 & status1 ==0:
            print(f"Send `{msg}` to topic `{topic_state}`")
            print(f"Send `{msg1}` to topic `{topic_brightness}`")
        else:
            print("failed to send message")
        msg_count += 2
        time.sleep(3)



def run():
    client = connect_mqtt()
    client.loop_start()
    publish(client)


if __name__ == '__main__':
    run()