from time import sleep
from dht import DHT22
from machine import Pin
import network
import machine
import socket

ssid = ""
password = ""

data_pin = Pin(28)
sensor = DHT22(data_pin)

relais_pin = Pin(15, Pin.OUT, value=0)

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

def webpage(relais_aan):
    html = f"""
            <!DOCTYPE html>
            <html>
            <body>
            <form action="./stekkerdoos-aan">
            <input type="submit" value="Stekkerdoos aan" />
            </form>
            <form action="./stekkerdoos-uit">
            <input type="submit" value="Stekkerdoos uit" />
            </form>
            <p>Stekkerdoos is {'aan' if relais_aan else 'uit'}</p>
            </body>
            </html>
            """
    return str(html)

def serve(connection):
    relais_aan = False
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request = str(request)
        print(request)

        try:
            verzoek = request.split()[1]
        except IndexError:
            pass
        if verzoek == '/stekkerdoos-aan?':
            relais_pin.on()
            relais_aan = True
        elif verzoek == '/stekkerdoos-uit?':
            relais_pin.off()
            relais_aan = False

        html = webpage(relais_aan)
        client.send(html)
        client.close()

try:
    ip = connect()
    print(f"Verbonden op {ip}")
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()