# Programma Cursusavond 6

Op cursusavond 6 gaan we zelf de p1 poort van een slimme meter uitlezen. Dit doen we met de ESP32 microcontroller van MakePico geprogrammeerd met MicroPython. We sturen de meetgegevens naar Home Assistant over MQTT. Deze avond is gebaseerd op het project [MicroPython p1 meter](https://github.com/Josverl/micropython-p1meter/) van Jos Verlinde.

## Aansluiten
Voor dit project heb je nodig:
* De ESP32 MakePico
* Het breadboard
* De RJ12 naar 6 Pins Dupont-Jumper Adapter - P1 Kabel
* 1 weerstand van 1k Ohm (zit in het losse, smalle deel van het breadboard gestoken)
* 3 Male to Male DuPont draden

1. Plaats de MakePico op het breadboard
2. Prik de RJ12 stekker in het breadboard
3. Sluit de volgende kabels aan:
    * Geel naar GP5
    * Groen naar GND
    * Zwart met de 1k Ohm weerstand ertussen naar GP15. De weerstand kun je in het breadboard steken.
![makepico esp32 aangesloten op de RJ12 stekker](images/makepico-p1-connected.png)

## Home Assistant voorbereiden voor MQTT

MQTT heeft een broker nodig, een applicatie die de gepubliceerde berichten naar de juist ontvangers verstuurd. Daarvoor moeten 3 stappen doorlopen worden in de HomeAssistant omgevingen:
1. We installeren een add-on die de broker Mosquitto installeert.
2. We maken een gebruiker aan voor MQTT.
3. We configureren de MQTT integratie.

### De Home Assistant omgevingen
Er zijn 4 NUCs die elke een Home Assistant hosten.
* Maak verbinding met het netwerk HomeAssistant, wachtwoord 12345678
* Gebruik de volgend links om bij HomeAssistant te komen:
    * http://ha2.local:8123
    * http://ha3.local:8123
    * http://ha4.local:8123
* De gebruikersnaam is admin, het wachtwoord is admin of gebruik het gebruikersnaam en wachtwoord wat je op avond 4 ingesteld hebt.

### Installeer de Mosquitto broker addon
1. Ga naar **Settings** en selecteer **Add-ons**
    ![home assistant addon overview](images/home-assistant-addon-store.png)
2. Klik op **Add-on store** en zoek naar **MQTT**
    ![home assistant addon store mqtt search](images/home-assistant-addon-store-mqtt.png)
3. Selecteer **Mosquitto broker** en klik **Install**
    ![home assistant addon store mosquitto install](images/home-assistant-addon-store-mqtt-install.png)
4. Na de installatie, selecteer **Start**
    ![home assistant addon store mosquitto start](images/home-assistant-addon-store-mqtt-broker-start.png)
5. Na het starten kun je de logs bekijken door bovenin op **Logs** te klikken. Als er "mosquitto version XXX running" staat, dan is die succesvol opgestart.
    ![home assistant addon store mosquitto logs](images/home-assistant-addon-store-mqtt-broker-logs.png)

### Maak een MQTT gebruiker aan
1. Ga naar **Settings** en selecteer **People**
    ![home assistant people overview](images/home-assistant-add-user.png)
2. Selecteer **Add Person** en voeg een nieuwe gebruiker toe genaamd *mqtt* en sta de persoon toe om in te loggen.
    ![home assistant add user](images/home-assistant-add-user-mqtt.png)
3. Stel een wachtwoord in voor de *mqtt* gebruiker, bijvoorbeeld *MQTTmqtt* en klik op **Create**
    ![home assistant add user password](images/home-assistant-add-user-mqtt-password.png)

### Configureer de MQTT integratie
1. Ga naar **Settings** en selecteer **Devices and integrations**. Onder **Discovered** staat de MQTT integratie, klik op **Configure**.
    ![alt text](images/home-assistant-integrations-discovered.png)
2. Klik op **Submit**.
    ![alt text](images/home-assistant-integrations-mqtt.png)
3. Open de instellingen van de MQTT integratie door in de lijst naar **MQTT** te gaan.
   ![alt text](images/home-assistant-integrations-mqtt-details.png)
4. Selecteer **Configure**
    ![alt text](images/home-assistant-integrations-mqtt-configure.png)
5. Selecteer **Reconfigure MQTT**
    ![alt text](images/home-assistant-integrations-mqtt-reconfigure.png)
6. Configureer de correcte gebruiker *mqtt* met wachtwoord *MQTTmqtt* en klik **Next**
    ![alt text](images/home-assistant-integrations-mqtt-reconfigure-broker.png)
7. Scroll naar beneden en klik **Submit**
    ![alt text](images/home-assistant-integrations-mqtt-reconfigure-submit.png)

Home Assistant is nu klaar voor MQTT.

## ESP32 configureren
1. Download de code als ZIP van het [MicroPython p1 meter](https://github.com/Josverl/micropython-p1meter/) project op GitHub
    ![alt text](images/esp32-download-code.png). Pak hem uit op je computer.
2. Sluit de MakePico aan op je computer
3. Open de `src` map in de uitgepakte zip in Thonny
    ![alt text](images/esp32-thonny.png)
4. **Configureer de interpreter**
    ![alt text](images/thonny-configureren-interpreter.png)
5. Selecteer **MicroPython ESP32** en klik op **Install or update MicroPython (esptool)**
    ![alt text](images/thonny-interpreter-esp32.png)
6. Selecteer de juiste poort, typisch een *USB Serial @ COM#*. Kies MicroPython family *ESP32*, variant *Espressif ESP32 / WROOM*. Klik op **Installeren**. MicroPython voor ESP32 wordt nu op je microcontroller geïnstalleerd.
    ![alt text](images/thonny-interpreter-install-firmware.png)
7. Open het bestand `config.py`. Zoek de volgende configuratie variabelen op en pas ze als volgt aan:
    ```python
    DEBUG = True
    RUN_SPLITTER = False
    homenet = {'SSID': 'HomeAssistant', 'password': '12345678'}
    broker = {'server': 'ha1.local', 'port': '1883', 'user': 'mqtt', 'password': 'MQTTmqtt'}
    HOST_NAME = b'homeassistant.p1_meter_JOUWNAAM'
    ```

    Kies bij de broker de home assistant installatie die je gebruikt, dus ha1.local, ha2.local, etcetera. Vervang in de HOST_NAME JOUWNAAM door je eigen naam. De HOST_NAME moet beginnen met `homeassistant`.
    ![alt text](images/thonny-config.png)
8. Upload alle bestanden in de `src` map naar je MicroPython apparaat:
    ![alt text](images/thonny-upload.png)
9. Plug je P1 stekker in een van de P1 repeaters.
10. Open het `main.py` bestand en selecteer `Start (F5)`:
    ![alt text](images/thonny-uitvoeren.png)
11. In de **Shell** wordt een heleboel output gelogd (we hebben immers de `DEBUG` logging op `True` gezet). Als alles goed gaat zie je dat de meterstanden uitgelezen worden en verstuurd worden via MQTT naar Home Assistant.
    ![alt text](images/thonny-output.png)

## MQTT waarden in Home Assistant weergeven
1. Open de instellingen van de MQTT integratie door in de lijst naar **MQTT** te gaan.
   ![alt text](images/home-assistant-integrations-mqtt-details.png)
2. Selecteer **Configure**
    ![alt text](images/home-assistant-integrations-mqtt-configure.png)
3. Onder **Listen to topic** vul het volgende onderwerp in: *homeassistant.p1_meter_JOUWNAAM/instant/consumption_kW*, waarbij je JOUWNAAM vervangt door wat je in de `config.py` ingesteld hebt. Klik op **Listen**
    ![alt text](images/home-assistant-luisteren-naar-onderwerp.png)
4. Na verloop van tijd zie je berichten over jouw topic verschijnen.
    ![alt text](images/home-assistant-receive-message.png)
5. Voor MQTT ondersteunde apparaten worden alle MQTT topics die beginnen met `homeassistant` automatisch ontdekt en toegevoegd als Device aan Home Assistant. Helaas stuurt de P1 meter nog niet de goede gegevens naar Home Assistant om automatisch te koppelen. Hier wordt nog aan gewerkt in het P1 meter project.

## Meer inzicht met MQTT Explorer
1. Download [MQTT explorer](https://mqtt-explorer.com/). Dit is een grafische tool om inzicht te krijgen in alle MQTT berichten die naar de MQTT broker gestuurd worden.
2. Maak verbinding met de MQTT broker op de door jouw gekozen Home Assistant server
    ![alt text](images/mqtt-explorer-connect.png)
3. Alle topics worden weergegeven
    ![alt text](images/mqtt-explorer.png)
