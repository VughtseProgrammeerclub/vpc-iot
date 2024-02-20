from time import sleep
from dht import DHT22
from machine import Pin
import network
import machine
import urequests

ssid = ""
password = ""

data_pin = Pin(28)
sensor = DHT22(data_pin)

def connect():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(ssid, password)
    while wlan.isconnected() == False:
        print("Wacht op verbinding...")
        sleep(1)
    ip = wlan.ifconfig()[0]
    return ip

try:
    ip = connect()
    print(f"Verbonden op {ip}")
    response = urequests.get("https://api.open-meteo.com/v1/forecast?latitude=51.6533&longitude=5.2943&current=temperature_2m,relative_humidity_2m")
    data = response.json()
    buiten_temperatuur = data["current"]["temperature_2m"]
    print(f"Actuele buiten temperatuur in Vught op 2 meter hoogte: {buiten_temperatuur}°C")
    
    sensor.measure()
    binnen_temperatuur = sensor.temperature()
    print(f"Actuele binnen temperatuur: {binnen_temperatuur}°C")
except KeyboardInterrupt:
    machine.reset()