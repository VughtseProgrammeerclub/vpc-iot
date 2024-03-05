from dht import DHT22
from machine import Pin
from time import sleep

data_pin = Pin(28)
sensor = DHT22(data_pin)
relais_pin = Pin(15, Pin.OUT, value=0)
relais_aan = False

while True:
    sensor.measure()
    temperatuur = sensor.temperature()
    print(temperatuur)

    if temperatuur > 20:
        relais_pin.on()
        relais_aan = True
    else:
        relais_pin.off()
        relais_aan = False
    
    sleep(5)
