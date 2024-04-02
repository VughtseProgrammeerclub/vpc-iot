# Programma Cursusavond 4

De vierde avond maken we kennis met het automatiseringsplatform Home Assistant. [Home Assistant](https://home-assistant.io) is een gratis, open source project waarmee je je smart home kan inrichten. Het beschikt over plugins voor ongeveer alle fabrikanten van consumenten domotica apparatuur, zodat elke apparaat uit te lezen en te besturen is via Home Assistant. Is er een koppeling voor een bepaald product nog niet, dan kan door de open natuur van de software zelf een plugin geschreven worden.

Dit is de opmaat naar Cursusavond 5, waar we onze eigen hardware gaan koppelen aan Home Assistant.

Deze avond begint met een presentatie om wat concepten van Home Assistant uit te leggen. Daarna splitsen we in 4 groepen op en gaan dan per groep zelf aan de slag om een nieuwe lege Home Assistant omgeving in te richten.

# Het inrichten van Home Assistant
Er zijn 4 NUCs die elke een Home Assistant hosten.
* Maak verbinding met het netwerk HomeAssistant, wachtwoord 12345678
* Gebruik de volgend links om bij HomeAssistant te komen:
    * Groep 1: http://ha1.local:8123
    * Groep 2: http://ha2.local:8123
    * Groep 3: http://ha3.local:8123
    * Groep 4: http://ha4.local:8123

* De gebruikersnaam is admin, het wachtwoord is admin
* Voeg eerst iedereen in de groep toe als "Person of Interest" onder "Settings" -> "People"
* Voeg een ruimte toe met jullie groepnaam (Settings -> Areas & Zones)
* Voeg de apparaten toe (Settings -> Devices & Services)
    * De Bluetooth temperatuur sensoren hebben een identifier op de achterkant geschreven. Kies de correcte sensor!
    * De lampen en het stopcontact zijn verbonden via Tuya. De Tuya integratie verloop via internet. Vraag Joep om verbinding te maken met zijn Tuya account, zodat je de apparaten in je Home Assistant te zien krijgt.
    * De SwitchBot apparaten worden automatisch gedetecteerd.
* Zorg dat de devices in de goede ruimte (jullie groepsnaam) zitten.
* Geef de apparaten op het dashboard weer
* Probeer Automations en Scenes te maken. Wees creatief!
* Je kan ook gebruik maken van de ingebouwde zonsopgang timing, of het weer.

# Links

* https://www.huizebruin.nl/home-assistant/xiaomi-mijia-thermometer-2-bluetooth-koppelen-aan-home-assistant/
* https://homeassistanttips.nl/2023/11/21/tuya-integratie-in-home-assistant/
* Home Assistant tips: https://www.youtube.com/watch?v=FVusYP4fHFM