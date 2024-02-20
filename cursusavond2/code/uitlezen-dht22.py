from dht import DHT22
from machine import Pin
from time import sleep

data_pin = Pin(28)
sensor = DHT22(data_pin)

while True:
    sensor.measure()
    temperatuur = sensor.temperature()
    luchtvochtigheid = sensor.humidity()

    print(f"Temperatuur: {temperatuur} graden")
    print(f"Luchtvochtigheid: {luchtvochtigheid}%")

    sleep(5)
