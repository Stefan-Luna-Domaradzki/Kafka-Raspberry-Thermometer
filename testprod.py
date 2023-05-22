from time import sleep
import json
import random
from datetime import datetime

from kafka import KafkaProducer

def GetCurrentTemperature():
    temperature_msg = random.randint(30, 32)
    return(temperature_msg)


def serializer(message):
    return json.dumps(message).encode('utf-8')


def message(arg) -> dict:

    return {'date': "obecna data", 'temperature': "temperatura"}


TemperatureProducer = KafkaProducer(
    bootstrap_servers=['192.168.1.218:9092'], #obecne IP mojego komputera w sieci lokalnej
    value_serializer=serializer,
    api_version=(3,3,1)
    )

if __name__ == '__main__':

    i = 0


    while True:

        Temperature = GetCurrentTemperature()

        print("wysylam temperature", Temperature)

        TemperatureProducer.send('Etherneet3.4', i+0.11)
        TemperatureProducer.flush()

        i += 1

        sleep(0.5)
