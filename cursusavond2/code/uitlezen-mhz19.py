from mhz19 import mhz19
from time import sleep

sensor = mhz19(0)

while True:
    if sensor.get_data():
        print(f"CO2 {sensor.ppm} ppm")
        print(f"Temperatuur: {sensor.temp} graden Celsius")
    else:
        print("Geen data ontvangen")
        
    sleep(5)