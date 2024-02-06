# Importeer de benodigde modules
import dht
from machine import Pin
import time

# Maak een DHT22-object dat verwijst naar pin 28
sensor = dht.DHT22(Pin(28))

while True:
    # Meet de sensorwaarden
    sensor.measure()
    temperatuur = sensor.temperature()
    luchtvochtigheid = sensor.humidity()  # Voeg deze regel toe

    # Toon de temperatuur en luchtvochtigheid
    print(f"Temperatuur: {temperatuur}°C, Luchtvochtigheid: {luchtvochtigheid}%")

    # Wacht 5 seconden voordat de volgende meting wordt uitgevoerd
    time.sleep(5)
