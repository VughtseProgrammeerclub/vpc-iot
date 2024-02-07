# Verslag Cursusavond 1

_Zie ook de [presentatie](VPC%20Cursusavond%201%20introductie%20Internet%20of%20Things%20in%20een%20Smart%20Home.pdf)._

We zijn de eerste cursusavond begonnen met een flinke club van 20 deelnemers. Na een korte introductie over de Vughtse Programmeerclub (opgericht in 2022 met een Cursus programmeren in Python, in 2023 in samenwerking met het Vughts museum en project gedaan). Uit een voorstelrondje onder de deelnemers blijkt de programmeerervaring te varieëren van 0 tot tientallen jaren en de home automation voorkennis van "ik wil leren wat er mogelijk is" tot professioneel installateur in het hogere segment. Een leuke combinatie waar we veel van elkaar kunnen leren.

Voor het [Internet of Things])(https://nl.wikipedia.org/wiki/Internet_der_dingen) zijn drie elementen nodig: **"dingen"** (apparaten), een **verbinding** (via wifi, bluetooth, etcetera) en een **controlesysteem**. Een voorbeeld: [het meten van de luchtkwaliteit in Nederland](https://www.samenmeten.nl/). Verschillende sensoren (de dingen) hangen verspreid over Nederland. Zij sturen hun data door via Wifi of LoraWan (de verbinding) naar het Data portaal van het RIVM (het controlesysteeem). In het controlesysteem wordt de data omgezet in een kaart met grafieken, die voor iedereen te raadplegen is.

Het Smart Home (ook wel [Domotica](https://nl.wikipedia.org/wiki/Domotica)) heeft dezelfde drie elementen: **"dingen"**, een **verbinding** (via wifi, bluetooth, zigbee of z-wave) en een **controlesysteem**. De "dingen" zijn gelimiteerd tot apparaten in het huishouden, de verbindingen zijn over korte afstand en de reikwijdte van het controle systeem is het huis en niet bijvoorbeeld heel Nederland. We kunnen zeggen dat het Smart Home een subset van het Internet of Things is.

Aan de hand van wat verschillende voorbeeldapparaten hebben we de verschillende soorten verbindingen besproken. Wifi heeft een groot bereik, het apparaat kan zelfstandig verbinden met het internet of huisnetwerk, maar verbruikt meer stroom. Bluetooth, Zigbee en Z-Wave hebben een laag stroomverbruik (sensoren of knoppen kunnen jaren op 1 batterijtje werken), maar hebben een veel korter bereik en er moet een Hub of Bridge gebruikt worden om te koppelen met het internet of huisnetwerk.

Ook de verschillende controlesystemen zijn aan bod gekomen. Elke fabrikant heeft zijn eigen app. Google en Apple proberen de verschillende apparaten te integreren in hun in elke telefoon ingebouwde Home software. Samsung en Homey bieden ook controlesystemen om alle apparaten te integreren. In de cursus gaan we gebruik maken van het controlesysteem Home Assistant, wat gratis en open source is.

Aan de hand van voorbeelden uit mijn eigen huis komen we tot vier redenen voor een Smart Home:
1. **Besparen** door inzicht te krijgen in (sluip)verbruik of het slim regelen van wanneer apparaten aan zijn.
2. **Comfort: Gezondheid** door het meten van het leefklimaat en daarop acteren.
3. **Comfort: Gemak** door veelvoorkomende taken te automatiseren of draadloos te bedienen.
4. **Veiligheid** door het in de gaten houden van je huis door middel van bijvoorbeeld slimme camera's, rookmelders, overstromingssensoren.

Na een korte pauze hebben we het programma van de cursus en de hardware doorgesproken. Dit overzicht staat in de [hoofd README van deze repository](../README.md).

Voor het programmeren in Python heb ik een paar bouwstenen behandeld van programmeren en gedemonstreerd hoe dat in Python werkt. Zie het bestand [voorbeelden-ingevuld.py](voorbeelden-ingevuld.py). Voor een introductiecursus Python raden we deze site aan: https://automatetheboringstuff.com/ (t/m hoofdstuk 3 is genoeg om mee te starten).

Daarnaast heb ik ook Artificial Intelligence gebruikt om het Python programmeren voor ons te doen. Hiervoor zijn [ChatGPT](https://chat.openai.com/) en [Microsoft CoPilot](https://copilot.microsoft.com/) geschikt. Bij een beschrijving van het gewenste programma, produceert de AI de code en geeft uitleg bij de code. Ze doen zelfs suggesties voor meer uitleg over de code of mogelijk uitbreidingen van de code. Ook kan de AI assistent gevraagd worden een door iemand anders geschreven stuk code uit te leggen.

Als laatste de praktische zaken:
1. We hebben de hardware pakketten verstrekt.
2. Het cursus materiaal is te vinden op https://github.com/VughtseProgrammeerclub/vpc-iot/
3. Om de communicatie te vergemakkelijken worden alle deelnemers toegevoegd aan de VPC Berichten WhatsApp groep. Deze groep bevat aankondigingen over de cursusavonden, maar mag ook gebruikt worden om onderling vragen te stellen.

De volgende sessie is dinsdag 20 februari om 20:00 in DePetrus.