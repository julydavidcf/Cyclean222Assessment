import random

from paho.mqtt import client as mqtt_client

#light-bulb
#brightness 0-100
bulb_brightness = 0;
# 0 = off; 1 = on
bulb_state = 0;

# I used a free public broker
broker = 'broker.emqx.io'
port = 1883
topic_state = 'smart-light-bulb/state'
topic_brightness = 'smart-light-bulb/brightness'
client_id = f'python-mqtt-{random.randint(0, 1000)}'
username = 'emqx'
password = 'public'


def connect_mqtt() -> mqtt_client:
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


def subscribe(client: mqtt_client):

    def on_message(client, userdata, msg):
        global bulb_state, bulb_brightness
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        if msg.topic == 'smart-light-bulb/state':
            bulb_state = msg.payload.decode();

        elif msg.topic == 'smart-light-bulb/brightness':
            bulb_brightness = msg.payload.decode();
        else:
            print("invalid message")
        printBulbState()

    client.subscribe(topic_state)
    client.subscribe(topic_brightness)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    subscribe(client)
    client.loop_forever()

def printBulbState():
    if bulb_state ==0:
        print("light Bulb is off")
    else:
        print("light Bulb is on")
    print("light bulb brightness is set to:" + str(bulb_brightness)+"\n");
    print("==============================")

if __name__ == '__main__':
    print("initial Bulb")
    printBulbState()

    run()