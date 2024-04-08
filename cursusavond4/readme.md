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
* Geef de apparaten op het dashboard weer.
* Probeer Automations en Scenes te maken. Bijvoorbeeld: als de temperatuur hoger is dan X graden celsius, kleur de lamp rood. Wees creatief!
* Je kan ook gebruik maken van de ingebouwde zonsopgang timing, of het weer.

# Links

* Online demo omgeving van Home Assistant: https://demo.home-assistant.io/#/lovelace/home
* Home Assistant installeren: https://www.home-assistant.io/installation/
* Home Assistant installeren op Windows met VMWare (uitdagend, maar geen Raspberry Pi of andere computer nodig): https://www.youtube.com/watch?v=jcxH9KwCRQE
* De Xiaomi Bluetooth Thermometer koppelen in Home Assistant: https://www.huizebruin.nl/home-assistant/xiaomi-mijia-thermometer-2-bluetooth-koppelen-aan-home-assistant/
* De lampen en sensoren die we gebruikt hebben, gebruikten het Tuya protocol. Ik heb ze handmatig toegevoegd in de Tuya Smart app en daarna ingelogd met mijn Tuya account in de home assistant installaties, zoals beschreven hier: https://homeassistanttips.nl/2023/11/21/tuya-integratie-in-home-assistant/
* De Home Assistant tips die ik aan het einde van de avond meegaf: https://www.youtube.com/watch?v=FVusYP4fHFM
* Home Assistant open zetten via het internet:
    * Makkelijkst maar betaald: via NabuCasa, de partij die HomeAssistant onderhoudt: https://www.nabucasa.com/
    * Makkelijk en gratis: met een CloudFlare tunnel: https://www.youtube.com/watch?v=xXAwT9N-7Hw
    * Via een VPN: https://www.youtube.com/watch?v=5rFWcukwCzU
    * Moeilijkst en minst veilig: Open zetten via je router, via DuckDNS en beveiligd met LetsEncrypt. Hierdoor wordt HomeAssistant bereikbaar voor iedereen op het internet, dus 2 factor authenticatie aangeraden: https://www.youtube.com/watch?v=AK5E2T5tWyM

# Verslag cursusavond 4

De 19 aanwezigen van avond 4 hebben een [presentatie Introductie Home Assistant](./VPC%20Cursusavond%204%20Introductie%20Home%20Assistant.pdf) gekregen. Hierin heb ik uitgelegd dat Home Assistant het probleem oplost dat elke fabrikant zijn eigen app heeft. Je gaat deze apps nog wel nodig hebben om de intiële setup te doen, maar vervolgens kun je de slimme apparaten integreren in Home Assistant. Voorbeeld: de slimme gordijnen van SwitchBot kun je het beste via de SwitchBot app installeren en kalibreren. Maar als dat eenmaal gedaan is, dan kun je in Home Assistant de gordijnen open en dicht doen.

De Home Assistant terminology:
* **Dashboard** is de startpagina van Home Assistant. Hierop heb je een snel overzicht van je slimme apparaten. Dashboards zijn naar eigen wens in te richten.
* **People** zijn de gebruikers van het systeem. Deze kunnen gekoppeld worden aan de Home Assistant App op hun telefoon.
* **Areas** zijn de ruimtes in je huis. Door je slimme apparaten toe te wijzen aan ruimtes, kun je bijvoorbeeld zeggen: doe alle lampen in de woonkamer uit.
* **Devices** zijn je slimme apparaten die met **integrations** aan Home Assistant gekoppeld worden. Home Assistant zoekt zelf via Wifi en Bluetooth naar apparaten. Het laat nog niet gekoppelde apparaten in een lijstje zien en heeft een tweede lijstje met al wel gekoppelde apparaten.
* **Automations** zijn een gebeurtenisen en actie systeem: als X gebeurd, doe dan Y. Bijvoorbeeld als de zon onder is, doe dan de buitenverlichting aan. De gebeurtenissen kunnen tijdsgebaseerd of sensor gebaseerd zijn. De acties doen typisch iets met de slimme apparaten.
* **Scenes** beschrijven een gewenste staat van je slimme apparaten. Bijvoorbeeld een "TV kijken" scene kan de TV aanzetten en de lampen dimmen. Scenes krijgen een knop op het dashboard zodat ze makkelijk geactiveerd kunnen worden.
* **Scripts** beschrijven een reeks stappen die in volgorde worden uitgevoerd. Bijvoorbeeld het script "opstaan" kan geleidelijk de verlichting feller laten branden en de gordijnen openen.
* **Blueprints** zijn deelbare configuraties van automations, scenes en scripts. Heb je een handige automatisering gemaakt en wil je die delen met de wereld? Dan kun je er een blueprint van maken. Je kan ook op het Blueprint forum van Home Assistant gebruik maken van automations die anderen gemaakt hebben.

De installatie van Home Assistant is een bewerkelijk klusje wat enige tijd kost. Dat had ik al voorbereid op 4 [NUCs](https://en.wikipedia.org/wiki/Next_Unit_of_Computing), zodat elke groep zijn eigen Home Assistant installatie had om in rond te klikken. Als eerste heeft iedereen in de groep een eigen account gemaakt. Stap twee was het maken van een eigen "ruimte" met de groepsnaam. Daarna konden we de slimme apparaten koppelen.

Omdat iedereen wel in dezelfde ruimte en op hetzelfde Wifi netwerk zat, waren alle Bluetooth sensoren en slimme apparaten zichtbaar in alle omgevingen, dus kon je stiekem ook de lampen van een andere groep aanzetten. De lampen volgen het Tuya protocol en heb ik gekoppeld in de Tuya Smart app. Daarna heb ik met mijn Tuya Smart account in Home Assistant ingelogd op een DigiD achtige manier: (1) vul in Home Assistant je account code uit de Tuya Smart app in, (2) scan met de Tuya Smart app de weergegeven QR code en (3) klik op Submit.

Uiteindelijk zijn er wat Automations en Scenes gemaakt. Voorbeeld: als de temperatuur van de Bluetooth sensor boven een bepaalde waarde komt, zet dan de lamp aan. Bij deze automation moest je opletten dat er op de slimme lamp geen actie "zet aan" is, maar dat daarvoor in de plaats de acite "zet lamp aan" moet kiezen en dan de slimme lamp als device mee moet geven.

Als laatste hebben we de avond afgesloten met nog wat Home Assistant tips voor de beginnende en gevorderde gebruikers.