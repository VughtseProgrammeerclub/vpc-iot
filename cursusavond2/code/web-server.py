from time import sleep
from dht import DHT22
from machine import Pin
import network
import machine
import urequests
import socket

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

def open_socket(ip):
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def webpage(buiten_temperatuur, binnen_temperatuur):
    html = f"""
            <!DOCTYPE html>
            <html>
            <body>
            <p>Buiten temperatuur is {buiten_temperatuur} graden Celsius</p>
            <p>Binnen temperatuur is {binnen_temperatuur} graden Celsius</p>
            </body>
            </html>
            """
    return str(html)

def serve(connection):
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        print(request)

        response = urequests.get("https://api.open-meteo.com/v1/forecast?latitude=51.6533&longitude=5.2943&current=temperature_2m,relative_humidity_2m")
        data = response.json()
        buiten_temperatuur = data["current"]["temperature_2m"]

        sensor.measure()
        binnen_temperatuur = sensor.temperature()

        html = webpage(buiten_temperatuur, binnen_temperatuur)
        client.send(html)
        client.close()

try:
    ip = connect()
    print(f"Verbonden op {ip}")
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()