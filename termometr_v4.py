import w1thermsensor
import json
from time import sleep
from kafka import KafkaProducer
from daterime import datetime

#import logging
#logging.basicConfig(level=logging.DEBUG)

#-- configure termomether sensor
sensor = w1thermsensor.W1ThermSensor()

temperature_producer = KafkaProducer(
    bootstrap_server=['host_ip:port'], #change to current host IP
    value_serializer=lamba v: json.dumps(v).encode('utf-8'),
    api_version=(3,3,1)
    )

if __name__ == '__main__':

    while True:

        kafka_topic = 'Ethernet3.3'

        temperature = sensor.get_temperature()
        print(temperature)

        temperature_producer.send(kafka_topic, temperature)
        print("sent")

        temperature_producer.flush()
        print("flushed")

        sleep(1)

