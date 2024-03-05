# Stekkerdoos via relais schakelen over het Wifi met de Raspberry Pi Pico W

*Voorkennis: dit project gaat er van uit dat je de [Stekkerdoos via relais schakelen met de Raspberry Pi Pico W](1-stekkerdoos-via-relais-schakelen-met-de-raspberry-pi-pico-w.md) en [Meetwaarden beschikbaar maken over Wifi door het opzetten van een webserver](../cursusavond2/4-opzetten-van-een-webserver-op-de-raspberry-pi-pico.md) voltooid hebt.*

**Haal de stekker uit het stopcontact voordat je verder programmert of aan de volgende opdracht begint!**

In dit project gaan we onze web-server uitbreiden met knoppen om de 

Voor dit project heb je nodig:
* De Raspberry Pi Pico W
* De micro USB kabel
* Het breadboard
* Het relais (blauw blok op PCB, in verpakking)
* De PCB voeding (zwart blokje met 2 gesoldeerde draden)
* 2 Wago verbinders met 3 aansluitingen
* 1 Wago doorverbinder met 2 aansluitingen
* 3 Male to Female DuPont draden
* 4 Male to Male DuPont draden

## Aansluiten
De aansluting is exact hetzelfde als [Stekkerdoos via relais schakelen met de Raspberry Pi Pico W](1-stekkerdoos-via-relais-schakelen-met-de-raspberry-pi-pico-w.md#aansluiten). We gaan enkel de software aanpassen.


## Programmeren
De gehele voorbeeld code is te vinden in [code/relais-schakelen-via-wifi.py](code/relais-schakelen-via-wifi.py).

We beginnen met de code van de webserver die we gemaakt hebben in de opdracht [Meetwaarden beschikbaar maken over Wifi door het opzetten van een webserver](../cursusavond2/4-opzetten-van-een-webserver-op-de-raspberry-pi-pico.md).

1. Kopieer het bestand [`web-server.py`](../cursusavond2/code/web-server.py) en hernoem het naar `relais-schakelen-via-wifi.py`.
2. Voeg onder de definitie van de DHT22 sensor pin de definitie van de relais_pin:
    ```python
    relais_pin = Pin(15, Pin.OUT, value=0)
    ```

3. We gaan een webpagina maken met twee knoppen en de huidige staat van de stekkerdoos. Vervang de huidige `webpage(buiten_temperatuur, binnen_temperatuur)` functie in zijn geheel voor de volgende, die een `relais_aan` parameter mee krijgt. We gebruiken een ternary operator om de boolean `relais_aan` te vertalen naar 'aan' of 'uit':
    ```python
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
    ```

4. We moeten de `serve(connection)` functie aanpassen om met het relais te werken en niet meer met de temperatuur. Verwijder als eerste alle temperatuur code:
    ```python
    def serve(connection):
        while True:
            client = connection.accept()[0]
            request = client.recv(1024)
            request = str(request)
            print(request)

            html = webpage()
            client.send(html)
            client.close()
    ```

5. Voeg als eerste regel van de functie de `relais_aan` staat toe:
    ```python
    def serve(connection):
        relais_aan = False
    ```

6. Vervolgens moeten we na de `print()` van het request code toevoegen die uit de url leest wat er met het relais moet gebeuren:
    ```python
            try:
                verzoek = request.split()[1]
            except IndexError:
                pass
    ```

7. En aan de hand van dat verzoek schakelen we de `relais_pin` en updaten we de status van het relais:
    ```python
            if verzoek == '/stekkerdoos-aan?':
                relais_pin.on()
                relais_aan = True
            elif verzoek == '/stekkerdoos-uit?':
                relais_pin.off()
                relais_aan = False
    ```

8. Zorg dat de html de nieuwe webpage functie aanroept met het `relais_aan` argument:
    ```python
            html = webpage(relais_aan)
    ```

9. Test het programma zonder de stekker er in te steken! Voer het programma uit door op de groene play knop te klikken. Open een webbrowser (Edge, Chrome of Firefox) en ga naar het gerapporteerde IP adres. Als het goed is zie je nu de webpagina met twee knoppen en de status van de stekkerdoos. Test de werking van de knoppen. Je moet het relais horen klikken.

> [TIP!]
> Als een device binnen een bepaalde tijd opnieuw bij een wifi netwerk verbindt, krijgt het hetzelfde IP adres als het eerst had. Gaat er echter te veel tijd overheen en is de zogenaamde DHCP lease verlopen, dan kan het zijn dat het device een ander IP krijgt. Als het device geen display heeft, zoals onze stekkerdoos, dan kunnen we niet zien wat het IP is. In dat geval moet je een vast IP adres instellen. Voor deze opdracht is dat echter niet nodig.

10. Hernoem je programma nu naar `main.py`.
11. Stop je draaiende programma met de stop knop.
12. Upload `main.py` naar de Raspberry Pi Pico W met Thonny. Dit gaat op dezelfde manier als een [library uploaden naar de Raspberry Pi Pico W](../cursusavond2/5-uitlezen-mhz19-co2-sensor-met-micropython.md#een-library-uploaden-naar-de-raspberry-pi-pico-w)).
13. Unplug de USB kabel van de Raspberry Pi Pico W.
14. Zet de schakelaar van je stekkerdoos aan.
16. Sluit de kabeldoos af door het deksel erop te doen. Let op dat je de kabels een plekje in het doosje geeft zodat ze geen kortsluiting maken.
17. Steek de stekker in het beveiligde stopcontact. Als alles goed aangesloten zit, krijgt de Raspberry Pi Pico W stroom vanuit de PCB voeding. De Raspberry Pi Pico W start op en gaat de geüploade `main.py` uitvoeren. De stekkerdoos is nu bereikbaar op het eerder gerapporteerde IP adres.
18. **Haal de stekker uit het stopcontact voordat je verder programmert of aan de volgende opdracht begint!**
