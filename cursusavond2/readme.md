# Programma cursusavond 2

* [Korte samenvatting avond 1](../cursusavond1/readme.md)
* [Introductie microPython + Thonny](1-introductie-raspberry-pi-pico-met-thonny.md): Raspberry Pi Pico aansluiten op de PC en de LED laten knipperen
* [De temperatuur en luchtvochtigheid uitlezen met de DHT22 sensor](2-uitlezen-dht22-temperatuursensor-met-micropython.md)
* [Verbinden met het Wifi](3-raspberry-pi-pico-w-verbinden-met-wifi.md)
* [Meetwaarden beschikbaar maken over Wifi door het opzetten van een webserver](4-opzetten-van-een-webserver-op-de-raspberry-pi-pico.md)
* [De CO2 sensor uitlezen](5-uitlezen-mhz19-co2-sensor-met-micropython.md)

# Verslag Cursusavond 2

Deze avond wederom 21 aanwezigen en een nieuwe locatie: Jeugd-en Jongerencentrum Elzenburg. Hier zaten we in een eigen ruimte, wat de akoestiek zeker ten goede kwam. Na een korte samenvatting van de presentatie van de eerste avond, werd het doel van deze avond uitgelegd: het programmeren van de Raspberry Pi Pico W. Sensoren uitlezen en daarna verbinding maken met het wifi. In Internet of Things termen: het "ding" (de Raspberry Pi Pico W met sensor) via een netwerkverbinding (het wifi) verbinden met een controlesysteem (de laptop).

Tijdens de eerste avond was de vraag binnen gekomen hoe het zat met de onderlinge compatibiliteit van de verschillende aanbieders van Smart Home devices. Om daar een stukje inzicht in te geven heeft Roel Beset een presentatie gegeven over een stage die die gedaan heeft waarin die precies dit uitgezocht heeft voor enkele apparaten. Na een bespreking van de testopstelling heeft Roel ons door zijn Excel sheet genomen met de testresultaten van de compatibiliteit van verschillende apparaten. Na het benoemen van enkele opvallende conclusies liet hij nog een keuzetabel zien waar je aan de hand van je wensen kan zien welke apparaten geschikt zijn. Bekijk [de Excel sheet met resultaten](Alecto-Connections.xlsx). Let op, dit onderzoek is alweer een paar jaar oud, dus kan niet meer helemaal actueel zijn. Ook zijn sommige producten niet meer beschikbaar.

Hierna gingen we aan de slag met de Raspberry Pi Pico W. Na de gebruikelijke opstartproblemen is het uiteindelijk iedereen gelukt om de temperatuursensor uit te lezen. Bij het opzetten van de server liepen we ertegenaan dat de netwerk beveiliging van het wifi geen verbindingen tussen machines onderling toestaat. Voor de volgende cursusavond zullen we een eigen netwerk meenemen zodat dit wel werkt. Wanneer je deze opdracht thuis doet zal dit geen probleem zijn.

De volgende cursusavond gaan we verder met de opdrachten en zullen er ook enkele nieuwe opdrachten zijn, zoals het schakelen van een relais.
