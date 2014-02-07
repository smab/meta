 SMAB: Statusrapport 19/12
===========================


## Sales pitch

  Playhouse är ett projekt som går ut på att göra om en byggnad till en stor
  interaktiv display där man kan visa såväl animationer som spela enklare spel
  genom ett webbgränssnitt.


## Projektbeskrivning

  Vi ska skapa ett system för att styra färgade lampor som ska sitta i
  fönster så att byggnaden blir en enorm skärm.  Skärmen ska kunna visa
  animationer och användas för att spela spel.  Animationerna ska enkelt kunna
  koreograferas med musik.  När skärmen är i spelläge så kan spelare ställa
  sig i en kö i ett webbgränssnitt, där de sedan eventuellt paras ihop med
  andra spelare för att kunna spela ett spel.


## Mål

  Att via ett webbgränssnitt låta användare spela ett spel där spelplanens
  pixlar består av fönster på en byggnad.  Vid en högre belastning ska
  spelarna ställas i kö.  Spelplanen ska visas för användaren med hjälp av en
  videoström av byggnaden och en virtuell spelplan för att minska problem med
  tidsfördröjning av videoströmmen.  Libido ska kunna ställa in vilket spel
  som användarna kan spela samt om det istället ska visas en animation på
  husfasaden samt hur denna animation ser ut.  Vi har också som mål att man i
  framtiden kan utvidga projektet för att hantera bygnader med speciella
  former.  Under detta projekt begränsar vi oss dock till rektangulära
  fasader.


## Förutsättningar (externa)

  * Vi måste använda lampor (troligtvis Hue eller Tellstick) som ska belysa
    fönstrena inifrån.
  * Interaktiv display.
  * Kösystem för spelare när de väntar.
  * Videoström av byggnaden som spelklienter kan se.


## Roller

  * Projektledare: Emil
  * Projektsekreterare: Markus
  * Kundrelationer: Arvid
  * Scrum Master: Emil
  * Product Owner: Arvid
  * Kvalitetssäkring: Alla
  * Utveckling: Alla


## Gruppbeskrivning

  Vi har bestämt oss för att jobba enligt den agila utvecklingsmetoden Scrum
  efter att ha jämfört olika metoder gäntemot varandra och mot de
  förutsättningar som gruppen har.  Detta beslut grundar sig på jämförelsen på
  http://www.nada.kth.se/~karlm/mvk/mvk09_lec3.pdf, som vi tycker verkar vara
  en tillförlitlig källa.


## Gruppmedlemmar

   Namn                   | Mail
  ------------------------|-----------------
   John Eriksson          | johne2@kth.se
   Arvid Fahlström Myrman | arvidfm@kth.se
   Jonas Höglund          | jhoglun@kth.se
   Hannes Leskelä         | hleskela@kth.se
   Christian Lidström     | clid@kth.se
   Mattias Palo           | mpalo@kth.se
   Markus Videll          | mvidell@kth.se
   Tomas Wickman          | tomaswic@kth.se
   Emil Öhman             | emiloh@kth.se


## Planering

### Aktiviteter

  * Utvärdera
    - Webbackendalternativ
    - "APIer"/kommunikationsvägar för Tellstick
    - APIer för Hue
    - Möjlighet att bädda in videoström i frontend (existerande
      streamingtjänster? Youtube?)

  * Producera komponenter
    - Lampserver
    - Webbserver-backend
    - Konfigurationsgränssnitt
    - Kö- och spelfrontend

  * API mellan lamp- och webbserver

  * Webbkamerabryggning till spelfrontend


### Beroendegraf mellan komponenter

  [TODO: bild]


### Milstolpar (och tidsplan)
* MS1 (December 2013)
  - [meta] Förstudie klar.
  - [lampor] Testprogram som styr Tellstick.

* MS2 (Januari 2014)
  - [config] Början på UI för konfigurering av animationer/spel
  - [lampor] Testprogram som styr Hue.
  - [lampor] Början på lampserverkod.
  - [lampor] Design av API/protokoll för kommunikation webbserver-lampserver
    klar.
  - [frontend] Början på UI för kösystem/spel.

* MS3 (Februari 2014)
  - [config] Stöd för: konfigurera enklare animationer, spela upp i
    gränssnittet.
  - [lampor] Lampserver kan styra bryggor och lampor för att ändra specifika
    lampor.
  - [webserver] Fungerande kösystem med turordning.
  - [frontend] Början på UI för kösystem/spel, kösystem fungerar och kopplad
    till server.

* MS4 (Mars 2014)
  - [config] Stöd för: spelkonfiguration med fyra i rad och tre i rad,
    möjlighet att spara inställningar till server.
  - [frontend] Fungerande spelgränssnitt, frontend klar.

* Att planera
  - Testning (animationer, synkronisering till musik, videoström i
    spelgränssnitt, load på kösystem, allmänt försöka paja kö- och
    spelgränssnittet).

Planeringen är preliminär, och är tänkt att ta hänsyn till vilka uppgifter som
beror på vilka, och potentiella risker som är associerade med olika moment.


## Research

Då den utrustning vi jobbar med är begränsad i antal behöver vi skapa en
gemensam testplats som vi alla kan nå utifrån. För att kunna göra detta har vi
behövt dels se till att vi faktiskt kan kontrollera utrustningen
programmatiskt, men också förbereda utrustning för att kunna skicka video från
testplatsen. Utrustningen vi har arbetat med är Telldus TellStick tillsammans
med ett antal strömbrytare som kan kontrolleras trådlöst, och för att kunna nå
testplatsen utifrån bestämde vi oss för att använda en Raspberry Pi kopplad
till en webbkamera. Vi har lärt oss att:

  * Den nätverksbaserade TellStick-modellen kan vanligtvis endast kontrolleras
    programmatiskt via ett online-API, som kräver att TellSticken är
    uppkopplad till Internet. Genom att installera en alternativ firmware blev
    det dock möjligt att kommunicera direkt med TellSticken över det lokala
    nätverket.

  * Strömbrytarna är opålitliga, på så sätt att de ofta inte reagerar när
    TellSticken skickar en signal. Dessutom verkar TellSticken i sig vara
    väldigt långsam, då det kan vara uppemot en halv sekunds paus mellan två
    signaler. Vi har därför bedömt att TellSticken antagligen inte är lämplig
    för mer avancerade animationer, såvida inte varje strömbrytare får en egen
    TellStick.

  * Raspberry Pi:n verkar inte stödja den webbkamera som vi hade planerat att
    använda. Vi kommer att bli tvungna att försöka med någon annan webbkamera,
    och om inte det fungerar kan vi bli tvungna att försöka hitta en annan,
    större server.

Som en alternativ till TellStick kommer vi enligt vår klients önskemål att
utforska Philips Hue. Medan den faktiska utrustningen ännu inte har anlänt,
har vi dock börjat titta på olika API:er för att sköta kommunikation med
Hue-bryggorna. Eftersom att vi kommer behöva kunna kommunicera med flera
bryggor samtidigt för att kunna uppnå tillräcklig räckvidd har vi primärt
tittat på API:er som har inbyggt stöd för kommunikation med flera bryggor.
Detta utesluter bland annat Philips egna officiella Java-API, vilket innebär
att vi istället har fått titta på alternativa tredjeparts-API:er. Vi har tills
vidare främst tittat på Python-baserade API:er, då vi redan använder Python på
annat håll i projektet. När Hue-lamporna anländer kommer vi att testa bland
annat pålitlighet, snabbhet och räckvidd för bryggorna.

Vad gäller webbservern har vi tittat på några olika Python-lösningar för att
bygga webbapplikationer. De vi tittat på är främst Django, Tornado och
CherryPy. För varje ramverk har vi byggt en simpel testapplikation för att få
en uppfattning av hur de fungerar. Vi har dock inte bestämt oss för vilket
ramverk vi ska använda ännu.


## Scenarier, krav och behov

### Scenarier

Glenn ska inviga en byggnad i centrala Göteborg och vill ha något spektakulärt
Han bestämmer sig för att anlita Libido Music för att installera lampor och
göra någon cool show. Libido kommer och installerar lampor i Glenns byggnad
samt gör en demo. Showen görs av Libido hos deras kontor vid Karlaplan och
visas på något sätt upp på invigningsdagen.

Karl-Bertil går förbi en cool byggnad i stan med massa lampor på. Han ser en
liten informationsskylt framför byggnaden som säger att om han går in på
example.com så kan han spela ett spel där han använder byggnaden som en stor
skärm. Han skriver in addressen och hamnar i en kö. Det står att han har plats
10 av 11.  Till slut kommer han att paras ihop med någon annan spelare och de
kan på ett enkelt sätt spela något spel.


### Krav

Användaren måste kunna

  * Skapa en animation
    - Synkroniserat med musik.
    - Tänder lampor i olika färger och styrkor (beroende på teknik)
    - Sätta färg, styrka, duration på lampor.

  * Spela enkla spel
    - Minst ett spel. Tick-tack-toe, 4-i-rad...
    - Med/mot varandra (och singleplayer?)
    - Spelare hamnar i en kö

  * Libido/byggnadsägaren ska ha möjlighet att enkelt administrera saken.
    - Byta spel samt konfigurera
    - Byta animation
    - Skärmsläckare (dvs animation) om ingen spelar?


### Behov

Inte absolut kritiskt, men trevligt i mån av tid.

  * Stödjer olika former på fasader.
  * Kan spara en ljusshow till fil så man kan skicka omkring den.
  * Automatisk hopkoppling om vart lamporna är
    - Tror dock detta blir onödigt svårt och lättare att bara säga till
      installören: “Sätt lampan med id 1 där!”
    - Testshow, som lyser upp lamporna i id-ordningen. Då kan man enkelt se om
      något har hamnat fel i installationen. 


## Teknologi/arkitektur

Vår applikation har två sorters användare: dels vår klient, som behöver kunna
skapa animationer etc., och dels vanliga personer som ansluter via en
webbläsare för att spela. För att kunna hantera flera spelare implementerar vi
ett kösystem, då det inte går att spela flera spelomgångar samtidigt. När en
spelare har nått längst fram i kön kommer spelaren att få se något gränssnitt
där den kan spela själva spelet samt livevideo som visar den faktiska
byggnaden där lamporna är installerade.

Detta innebär att det behövs någon sorts webbserver som har som funktion att
skicka individuella sidor till användaren, samt som hanterar kö- och
spellogiken. Vi har bestämt oss för att använda Python genom
uteslutningsmetoden: språk som C++, Java och Haskell ansågs något opassande
för ändamålet, och PHP fick högljudd kritik från vissa gruppmedlemmar. Kvar
var språk som Python, JavaScript (node.js) och Ruby, och då gruppen kollektivt
verkade ha mer erfarenhet av Python blev det vårt val. 

Vi behöver också någon komponent så hanterar kommunikation med de bryggor som
i sin tur kommunicerar direkt med lamporna. Vi ansåg att det vore lämpligt att
implementera webbkomponenten och lampkommunikationskomponenten som två
separata servrar.

Då vi behöver kunna visa livevideo från byggnaden kommer vi också att behöva
kunna kommunicera med någon server som är kopplad till en kamera.


  [TODO: bild]


## Risker

Risk | Åtgärd | Sann. | Impact
-----|--------|-------|----------
Kommunikation mellan bryggor och lampor är opålitlig (väldigt stor fördröjning, tappar signaler, etc.) | Fixa eventuella buggar; Använda fler bryggor vid behov | Hög | Hög
Kommunikation mellan lampservern och bryggorna är bristfällig (för långsam/opålitlig) | Fixa eventuella buggar; Fixa diverse tekniska problem med anslutning | Medel | Hög
Lamporna stör varandra när de har olika färger (t.ex. två fönster inom samma rum) | Skärmar mellan lamporna; Begränsa så att lampor i samma rum alltid har samma färg | Låg | Medel
Problem med ihopkopplingen av delsystem(lamp- och webbserver etc.) (interna protokoll matchar inte, inkorrekt data, etc.) | Fixa eventuella buggar | Medel | 11/10
Webbservern och/eller webbgränssnittet är instabila | Fixa eventuella buggar | Medel | Medel
Webbservern får fler besökare än den kan hantera (överbelastning, stort intressen, DoS) | Köra webbserver i molnet (Amazon eller liknande); Optimera koden lite; Stäng av spel och spela animation istället (ej interaktiv dock); Iptables-magi? (droppa paket) | Låg | Medel
Osynkade animationer (lampor byter färg i varierande hastigheter så att lamporna är i osynk med varandra) | Använda fler bryggor; Begränsa animationerna så att de inte är för beroende av perfekt synk | Medel | Medel
Webbkamerastreaming fungerar dåligt (lamporna syns dåligt, dålig bildkvalitet, laggigt, ingen bild alls, kameran ramlar ner) | Fixa eventuella buggar; Bättre Internetuppkoppling; Bättre kamera; Bättre kamerainstallation | Medel | Medel
Huset syns dåligt i webbkameran p.g.a väderleksförhållanden eller liknande, t.ex. regn eller dimma. | [Bättre väder][1]; Stänga av Playhouse när det är dålig sikt | Låg | Låg

[1]: http://en.wikipedia.org/wiki/Weather_modification
