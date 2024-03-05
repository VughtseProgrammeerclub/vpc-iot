from machine import Pin
from time import sleep

relais_pin = Pin(15, Pin.OUT, value=0)
relais_aan = False

while True:
    if relais_aan:
        relais_pin.off()
        relais_aan = False
    else:
        relais_pin.on()
        relais_aan = True
    
    sleep(5)
