import paho.mqtt.client as paho
import time

broker_ip = "broker.emqx.io"
broker_port = 1883
topic = "same/topic"

publishName = "pub1"


# def on_publish(client, userdata, result):  # create function for callback
#     print("data published \n")
#     pass


def on_disconnect(client, userdata, rc):
    print("\nClient Disconnected ")


def createClient(insatanceName):
    client = paho.Client(insatanceName)  # create client object
    # client.on_publish = on_publish  # assign function to callback
    client.connect(broker_ip, broker_port)  # establish connection
    return client


try:

    print("Start service")
    print("to Stop service press CTRL + C\n")

    client = createClient(publishName)

    for count in range(0, 5):
        dataPayload = str(count)
        pub_status = client.publish(topic, payload=dataPayload)
        if pub_status[0] == 0:
            print("Data {} published".format(dataPayload))
        time.sleep(2)  # Delay 1 second

except KeyboardInterrupt:
    client.on_disconnect = on_disconnect
    client.disconnect()
    print("Service Stop")
