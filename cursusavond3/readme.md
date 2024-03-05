# Programma cursusavond 3

Op deze derde avond gaan we met de Raspberry Pi Pico W een stekkerdoos schakelen. De opdrachten van avond 3 bouwen voort op de opdrachten van avond 2. Hieronder zie je de volgorde van de opdrachten. Het is dus niet nodig om alle opdrachten van cursusavond 2 af te hebben, voor je aan de opdrachten van avond 3 begint.

* [Samenvatting avond 2](../cursusavond2/readme.md)
* Avond 2: [Introductie microPython + Thonny](../cursusavond2/1-introductie-raspberry-pi-pico-met-thonny.md): Raspberry Pi Pico aansluiten op de PC en de LED laten knipperen
* Avond 2: [De temperatuur en luchtvochtigheid uitlezen met de DHT22 sensor](../cursusavond2/2-uitlezen-dht22-temperatuursensor-met-micropython.md)
* Avond 3: [Stekkerdoos via relais schakelen](1-stekkerdoos-via-relais-schakelen-met-de-raspberry-pi-pico-w.md)
* Avond 2: [Verbinden met het Wifi](../cursusavond2/3-raspberry-pi-pico-w-verbinden-met-wifi.md)
* Avond 2: [Meetwaarden beschikbaar maken over Wifi door het opzetten van een webserver](../cursusavond2/4-opzetten-van-een-webserver-op-de-raspberry-pi-pico.md)
* Avond 3: [Stekkerdoos via relais schakelen via het Wifi](2-stekkerdoos-via-relais-schakelen-via-wifi.md)
* Avond 2: [De CO2 sensor uitlezen](../cursusavond2/5-uitlezen-mhz19-co2-sensor-met-micropython.md)
* Avond 3: [Stekkerdoos via relais schakelen op basis van temperatuur](3-stekkerdoos-via-relais-schakelen-op-basis-van-temperatuur.md)

# Verslag Cursusavond 3

De derde avond was weer goed gevuld, met 19 aanwezigen en een andere ruimte in Jeugd-en Jongerencentrum Elzenburg. Zoals hierboven te zien zijn de opdrachten van avond 3 door de opdrachten van avond 2 heen gewoven. Zo kun je ook als je nog niet alles van avond 2 gedaan had, toch met het relais aan de slag.

Na een korte introductie met een [veiligheidsinstructie over het werken met 230 volt](1-stekkerdoos-via-relais-schakelen-met-de-raspberry-pi-pico-w.md#stekkerdoos-via-relais-schakelen-met-de-raspberry-pi-pico-w), hebben we de stekkerdozen uitgereikt en kon iedereen aan de slag met de opdrachten.

Voor het aansluiten van het relais was er wat knutselwerk aan de hardware nodig. Vooral het routeren van de draadjes was een uitdaging om de PCB voeding goed in het breadboard te krijgen. Deze is eigenlijk meer geschikt om vast te solderen op een printplaat. En er zat een verkeerde foto in waarop een draadje verkeerd aangesloten was. Dit is gecorrigeerd in de handleiding.

Uiteindelijk heeft vrijwel iedereen het relais aan het schakelen gekregen. Dit kon veilig getest worden zonder 230 volt. Na een controle door de begeleiding hebben enkelen het zelfs aangedurfd om hun project en programma op 230 volt te testen. Dit werd gedaan op een stopcontact waar een gloeilamp in serie aangesloten zit. In geval van kortsluiting gaat de gloeilamp branden en slaan de stoppen niet uit. Deze voorzorgsmaatregel was gelukkig niet nodig.

Het eigen netwerk wat we bij ons hadden om de netwerk beveiliging van het wifi die geen verbindingen tussen machines onderling toestaat te omzeilen, werkt niet vlekkeloos. Zodoende gingen de opdrachten over het wifi nog steeds niet goed. Sommigen gebruikten het hotspot van hun telefoon om zowel Raspberry Pi Pico W en laptop op aan te sluiten en hadden daar wel succes mee. Waarschijnlijk was 40 verbindingen tegelijk (laptops + Picos) te veel van het goede voor het access point. Volgende keer nemen we een beter access point mee. Wanneer je deze opdracht thuis doet zal dit geen probleem zijn.

Volgende cursusavond (2 april) gaan we aan de slag met Home Assistant.