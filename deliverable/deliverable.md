 SMAB: Statusrapport 3/3
==========================

## Changelog

  * 7/2:  reviderade dokumentet för att matcha förändringar i projektets
          utveckling och förlopp. (Jonas, John, Emil)
  * 13/2: lade till rubrikerna *Dokumentation* och *Träning*, justerade
          formuleringar och lade till skisser.
  * 3/3:  uppdaterade research delen genom att lägga till vad vi efterforskat om 
          gif-parsers och livestreamingtjänster.
  * 3/3:  uppdaterade research om Gif-parser, streamingtjänst samt räckvidd på
    	  hue-lamporna samt deras bryggor.
  * 7/3:  drygade ut de olika texterna.
  * 10/3: la till länkar och redigerade demo 2 samt hue-testet. La in
    	  placeholder för MS 5 i april.
  * 23/3 La till lite information om de olika streamingtjänsterna och deras prisplaner samt pillade lite
         på milstolpe 5

## Sales pitch

  Playhouse är ett projekt som går ut på att göra om en byggnad till en stor
  interaktiv display där man kan visa såväl animationer som spela enklare spel
  genom ett webbgränssnitt. På så sätt kan företag uppmärksamma sina byggnader
  på ett innovativt sätt och användare får delta på ett unikt sätt.


## Projektbeskrivning

  Vi ska skapa ett system för att styra färgade lampor som ska sitta i
  fönster så att byggnaden blir en enorm skärm.  Skärmen ska kunna visa
  animationer och användas för att spela spel.  Det ska gå att i ett senare
  skede koppla elektroniska instrument (exempelvis synth) så att de utöver
  att spela upp ljud också ändrar lamporna.  När skärmen är i spelläge så kan
  spelare ställa sig i en kö i ett webbgränssnitt, där de sedan eventuellt
  paras ihop med andra spelare för att kunna spela ett spel.


## Mål

  Att via ett webbgränssnitt låta användare spela ett spel där spelplanens
  pixlar består av fönster på en byggnad.  Vid en högre belastning ska
  spelarna ställas i kö.  Spelplanen ska visas för användaren med hjälp av en
  videoström av byggnaden och en virtuell spelplan för att minska problem med
  tidsfördröjning av videoströmmen.  Libido ska kunna ställa in vilket spel
  som användarna kan spela samt om det istället ska visas en animation på
  husfasaden samt hur denna animation ser ut.  Vi har också som mål att man i
  framtiden kan utvidga projektet för att hantera byggnader med speciella
  former.  Under detta projekt begränsar vi oss dock till rektangulära
  fasader.


## Förutsättningar (externa)

  * Vi måste använda lampor (troligtvis Hue) som ska belysa fönstren inifrån.
    - Kunden måste tillhandahålla hårdvara att arbeta med
  * Interaktiv display.
  * Kösystem för spelare när de väntar.
  * Videoström av byggnaden som spelklienter kan se.


## Proof-of-concept

  En demonstration av spelet tic-tac-toe demonstrerades den 29e januari i KTHs
  lokaler på en fasad med nio fönster efter önskemål från kund utav detta.
  Detta demo bekräftar att projektidén med lampor i fönster fungerar som
  tänkt.
  Ytterligare en demonstration presenterades den 6e mars där kunden fick se
  framstegen vi gjort både på front-end och indirekt även back-end. Tic-tac-
  toe demonstrerades återigen, tillsammans med animationskapaciteten och 
  konfigurationsgränssnittet där man lägger till och testar bryggor.


## Roller

  * Projektledare: Emil
  * Projektsekreterare: Markus
  * Kundrelationer: Arvid
  * Scrum Master: Emil
  * Product Owner: Arvid
  * Kvalitetssäkring: Alla
  * Utveckling: Alla


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


## Utvecklingsmetod

  Vi har bestämt oss för att jobba enligt den agila utvecklingsmetoden Scrum
  efter att ha jämfört olika metoder gäntemot varandra och mot de
  förutsättningar som gruppen har.  Detta beslut grundar sig på jämförelsen på
  http://www.nada.kth.se/~karlm/mvk/mvk09_lec3.pdf, som vi tycker verkar vara
  en tillförlitlig källa.

  Vi har valt att använda väldigt korta sprinter för att få mer finkornig
  kontroll över vad som görs och snabbt kunna hantera problem som uppstår om
  något tar längre tid än beräknat eller blir försenat.  Gruppmedlemmarna är
  överens om att de snabbare sprinter ger ökad effektivitet i arbetet.
  
  Under projektets gång förkortade vi sprinterna ytterligare. Inledningsvis
  arbetade vi med veckolånga sprinter, något vi senare kortade ner ytterligare
  då vi ansåg att arbetsbördan blev för liten. Beroende på arbetsuppgifter
  arbetar vi i sprinter som är mellan 4-7 dagar långa för att få en så 
  bra tid/resultat ratio som möjligt.

## Planering

### Aktiviteter

  * Utveckla lampserver
    - Implementera JSON-API

  * Utveckla spelbackend
    - API för spelmoduler
    - Implementera tic-tac-toe som spelmodul
    - Implementera fyra-i-rad
    - Implementera animationsmöjligheter

  * Utveckla spelfrontend
    - Sätta upp websocket-kommunikation

  * Utveckla kösystem
    - Motverka botar

  * Utvärdera
    - Lampteknik (lampräckvidd mm)
    - Möjlighet att använda GIF
    - Design av eget filformat?
    - Inbäddning av videoström i spelfrontend

  * Dokumentera
    - Lampinstallation
    - Projektets arkitektur (separat)
    - Installation av komponenter


### Beroendegraf mellan komponenter

  ![Komponentberoendegraf](https://github.com/smab/meta/raw/master/deliverable/task-dependencies.png)

### Milstolpar (och tidsplan)

Milstolpar under projektets gång redovisas nedan.  Milstolparna
MS1 och MS2 har uppnåtts under tidigt skede i projektet och visas därmed ej
nedan.

* MS3 (Februari 2014)
  - [lampor] Lampserver kan styra bryggor och lampor för att ändra specifika
    lampor.
  - [webserver] Fungerande kösystem med turordning.
  - [frontend] Början på UI för kösystem/spel, kösystem fungerar och kopplad
    till server.

* MS4 (Mars 2014)
  - [config] Stöd för: spelkonfiguration med fyra i rad och tre i rad,
    möjlighet att spara inställningar till server.
  - [frontend] Fungerande spelgränssnitt, frontend klar.

* MS5 (April 2014)
  - [generellt] Bugfixa skriven kod
  - [generellt] Kommentera skriven kod

Planeringen är preliminär, och är tänkt att ta hänsyn till vilka uppgifter som
beror på vilka, och potentiella risker som är associerade med olika moment.


## Forskning

  Efter att ha utvärderat Hue-lamporna så har vi kommit fram till att dessa är
  betydligt bättre lämpade för vårt ändamål än tekniken Tellstick.  Fördelar
  med Hue-tekniken är bland annat bättre stabilitet, starkare lampor, bättre
  stöd för olika färger samt färdiga APIer som vi kan kommunicera med.  Vi har
  beslutat oss för att skriva backenden i Python, och har implementerat kod
  för att kommunicera med Hues lampservrar över HTTP via deras REST-API som
  använder JSON.

  Vi har satt upp en gemensam testplats och en testrigg med nio hue-lampor.
  Riggen är i KTHs lokaler, och vi har satt upp en kamera som streamar
  lampornas status.  Tellsticktekniken återanvänds för att kontrollera
  eltillförseln till riggen, så att lamporna kan stängas av när de inte
  används.  Lamporna kan kontrolleras utifrån, vilket gör det möjligt att
  testa ändringar utifrån.

  Vi har börjat undersöka idén att använda GIF-animationer för lagring av våra
  animationer, där tanken är att vi slipper skriva ett eget verktyg för att
  skapa animationer om det redan finns kompetenta sådana.  Istället tänker vi
  lägga större vikt på lampserverkomponenten och att få animationer att
  synkroniseras bra.  Vi har kollat på ett par olika animationsverktyg och
  konstaterat att det verkar finnas tillräckligt bra sådana tillgängliga.  En
  del tekniska bekymmer kvarstår, så som skillnaden på färgspektrum för GIF
  och våra Hue-lampor.  Vidare studier inom detta område behöver göras.

## Forskning: Backend
   
   När vi inledningsvis diskuterade vilka språk som vi skulle använda för de
   olika delarna i projektet så var det främst python som förespråkades.
   Då det var få av oss som hade några krav på vilket språk som skulle
   användas och några gruppmedlemmar dessutom hade goda kunskaper inom python
   så valde vi just detta för backend. Därefter påbörjade vi efterforskningar
   för att hitta ett lämpligt bibliotek för backenden, där krav låg på att
   hantera många bryggor och aktiva anslutningar.
   Tre gruppmedlemmar undersökte lika många bibliotek som vi gemensamt hade
   diskuterat fram som lämpliga: Django, CherryPy samt Tornado.
   
   Django bygger på designmönstret Model-View-Controller och kommer på
   förhand med diverse användbara applikationer och egenskaper. Till exempel
   så är det rekommenderat att låta Django bygga skalet för hemsidan, något
   som görs automatiskt. Därefter utvecklar man sidan i ett pythonliknande
   templatingspråk. Därtill skapas en adminkonsol som fungerar som ett sorts
   CMS, något som underlättar vid frekvent modelering av innehåll.
   Däremot tror vi inte att dessa funktioner är nödvändiga eller ens 
   lämpliga för vårt projekt.
      
   Det andra biblioteket som vi undersökte och till sist valde var Tornado.
   Detta beslut grundar sig på att Tornado enligt jämförelser och
   designfilosofi har som mål att klara höga belastningar samt bra inbyggt 
   stöd för tekniker så som websockets som
   vi ämnar att använda.

   Det sista alternativet vi undersökte var CherryPy. Biblioteket i sig
   var lättanvänt, till exempel så kunde man definiera flera funktioner i
   varje klass och sedan anropa dessa via URL:en /funktionsnamn. Detta i 
   motsats till Tornado där varje klass måste vara i en egen fil och man
   anropade dess klass-URL istället. Dock så hade inte CherryPy ett inbyggt
   stöd för websockets, något som gjorde att vi rankade Tornado högre.


## Forskning: Räckvidd på Hue-lampor
   
   För att klargöra eventuella problem i driftsatt tillstånd testade vi Hue-
   lampornas räckvidd vid olika scenarion. Detta genomfördes på KTH som har
   relativt tjocka betongväggar på ca 50 cm och likartade golv.
   Testet utgick ifrån ett script som fick lamporna tillhörande en brygga att
   blinka en gång varannan sekund i en klarblå nyans. Därefter undersökte vi
   räckvidden från brygga till lampa under följande scenarion:

   * Utan hinder 
   * Antal väggar
   * Antal golv
   * Antal golv och väggar 

   När en lampa (A) inte fungerade testade vi också att sätta en annan lampa (B)
   mellan A och bryggan, för att på så sätt att repeater-delen fungerar bra. Med
   repeaterdelen  vill vi i framtiden också testa gruppfunktionaliteten, se så
   att man fortfarande kan få dem att blinka synkat.
   Dessvärre kunde vi inte testa lamporna genom golv mer än vad som redan 
   gjorts under demot den 29.e januari. Detta för att det inte gick att flytta 
   på bryggorna och få internetanslutning på den nya platsen. Detta berodde 
   förmodligen på att de fick en annan ip adress än den vi skickade våra 
   meddelanden till, något som kanske berodde på KTH:s nätverksstruktur.
   
   Resultatet av de övriga testerna var någorlunda hoppfulla för vårt ändamål.
   Sedan tidigare visst vi att bryggan klarar av att skicka sina signaler genom
   KTH:s golv. Även genom en vägg fungerade väl, men vi märkte direkt att
   ytterligare obstruktion gjorde att signalerna förlorades antingen periodvis
   eller fullständigt. 
   Därefter fortsatte vi genom att testa repeatereffekten hos hue-lamporna. 
   Utan hinder så kunde vi konstatera att varje lampa kunde skicka signalen
   cirka 20 meter utan att några fördröjningar uppstod. Längre än så kunde man
   inte garantera synkroniserat blinkande.
   Därefter fortsatte vi genom att testa hue-lampornas repeatereffekt genom
   väggar. 
   //TODO fortsätta


   Det som kvarstår att testa är således hur många lampor man kan seriekoppla 
   och eventuella delays som ett resultat av detta, samt att seriekoppla genom 
   golv.
   

## Forskning: Gif-parser

   För att hantera skapandet av animationer har vi valt att skapa gif-bilder
   vid varje animationssteg för att sedan tolka dessa på ett sätt som
   lamporna kan förstå. Det huvudsakliga resultatet ifrån denna efterforskning
   ledde till användandet av pythonbiblioteket Pillow, en fork av PIL, som har
   väl definierade metoder att nyttja för att implementera de funktioner
   vi behöver.
   Vår kravspec inkluderade att kunna:
   * Läsa in en bild
   * Byta frame
   * Läsa in längd av en frame
   * Observera en enskild pixel
   * Hämta information från enskild pixel

   Andra bibliotek som undersöktes inkluderade:
   * Mahotas 
   * Scikit-Image
   * Insight Segmentation and Registration Toolkit(ltk) 
   * OpenCV
   * Medical image processing in Python (MedPy)

   Då Pillow hade allt vi behövde och var enkelt att implementera blev det
   ingen större debatt kring valet av bibliotek, utan vi implementerade en gif-
   parser med hjälp av detta bibliotek.

## Forskning: Stream-tjänster

  Vi har arbetat med idén att använda GIF-animationer för lagring av våra
  animationer, där tanken är att vi slipper skriva ett eget verktyg för att
  skapa animationer då det redan finns kompetenta sådana som vi funnit efter 
  en del efterforskningar.  Istället tänker vi lägga större vikt på 
  lampserverkomponenten och att få animationer att synkroniseras bra.  Vi har
  kollat på ett par olika animationsverktyg och konstaterat att det verkar
  finnas tillräckligt bra sådana tillgängliga. En del tekniska bekymmer 
  kvarstår, så som skillnaden på färgspektrum för GIF och våra Hue-lampor.
  Vi har hittat gif-verktyg som verkar passa våra behov bra. Då det enda vi
  egenligen eftersöker är ett enkelt gränssnitt för att skapa simpla 
  animationer så spelar det inte så stor roll om det saknar en del 
  funktionalitet. Likt livstreamingtjänsen så kommer det i slutändan inte 
  vara vi som kommer behöva tilhandahålla ett gifanimeringsverktyg utan vi 
  ska bara tillföra möjligheten att kunna ladda upp gifanimationer till 
  servern så att denna spelar upp animationen till lamporna. Vi har dock 
  genomfört en del forskning inom verktyg och kommit fram till att Asesprite 
  verkar som ett lämpligt verktyg för att utföra de tester som vi behöver 
  utföra. Det är dessutom släppt med öppen källkod på programmet vilket vi 
  tycker är ett plus.
  
  Vi har diskuterat olika livestreamingtjänster inom gruppen som verkar 
  lämpliga, men det är svårt att dra några slutsater i detta skede då det 
  ligger utanför våran arbetsbeskrivning att implementera en streamingtjänst.
  Men att på ett enkelt sätt tillhandahålla möjligheten att implementera en 
  livestreaming på våran hemsida känns som en relevant och överkomlig uppgift.
  
  De livestreamingtjänster och program för inspelning som vi diskuterat inom 
  gruppen är som följer med sin för/nackdelar:

Dessa program används till att streama  

  * XSplit
   - Betallösning
   - Endast Windows

  * OBS (Open Broadcaster Sowftware)
   - Gratis
   - Windows, Linux kommer släppas
 
  * FFSplit
   - Gratis
   - Windows

  * Wirecast
   - Betallösning
   - Windows, Macintosh

  * FFmpeg
   - Gratis
   - Windows, Macintosh, Linux
   - Kommandorad
   - Massa bra info, bla om tidsfördröjning och hur man kopplar ihop med twitch. https://
   trac.ffmpeg.org/wiki/StreamingGuide
 
 * Simple Screen Recorder
  - Gratis
  - http://www.maartenbaert.be/simplescreenrecorder/live-streaming/
  - Kommandorad, och vanligt
  - Kan vara buggigt

Följande företag tillhandahåller streamingtjänster

 * Livestream
  - Gratis men med möjlighet att betala för mer tjänster.
  Dessa verkar dock mest ha att göra med att man far tillgång till deras
  videoredigeringsverktyg
  - http://new.livestream.com/plans

 * Bambuser
  - Har gratis alternativ som inte är ett alternativ för våran applikation
  - Kostnaden hänger ihop med hur många tittartimmar som man vill köpa
  och överstiger man dessa timmar sa kostar det extra per timma
  - http://bambuser.com/premium

 * Ustream
  - Gratisalternativ for privatpersoner
  - Baserar sig ocksa pa tittartimmar
  - För deras 'Enterprise' prisplan far man kontakta dem
  - https://www.ustream.tv/platform/plans#itm_source=footer&itm_medium=plans_pricing_link&itm_content=Plans_and_Pricing&itm_campaign=footer

 * Justin.tv
  - Baserar sig på tittartimmar
  - även dessa har ett enterprisealternativ
  - http://www.justin.tv/payments/premium/
 
 * Twitch
  - Verkar rätt nischat på spel
  - Har ingen riktig betalplan men man kan bli 'twitch partner' för diverse fördelar
  - http://www.twitch.tv/p/partnersvideo


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
    - Tänder lampor i olika färger och styrkor
    - Sätta färg, styrka, tidsfördröjning på lampor.

  * Spela enkla spel
    - Minst ett spel. Tic-tac-toe, 4-i-rad...
    - Mot varandra
    - Spelare hamnar i en kö

  * Libido/byggnadsägaren ska ha möjlighet att enkelt administrera
    installationen.
    - Byta spel samt konfigurera färgval
    - Byta animation
    - Skärmsläckare (dvs animation) om ingen spelar?

Se även tidigare avsnitt om projektets externa förutsättningar.


### I mån av tid

  * Stöd för olika form på fasader
    - I dagsläget förutsätter vi rektangulära husfasader, men i praktiken kan
      många aktuella hus ha ickerektangulär fasad.  I sådana fall är det
      önskvärt att på något sätt kunna ange utseendet på fasaden.

  * Förenkla hopkoppling mellan lampor och bryggor
    - Idag behöver man koppla samman lampor med bryggor genom att skruva i en
      i taget och köra ett program mellan varje lampa.  Det skulle förenkla
      installation av lampor i byggnad avsevärt om man kunde skruva i alla
      lampor på en gång och sedan via ett gränssnitt mappa lamporna till
      pixlar.
    - För att verifiera att allt satts upp i rätt ordning vore det användbart
      med ett testprogram som lyser upp lamporna enligt ett förbestämt
      mönster, ex. rad för rad och kolumn för kolumn.


## Teknologi och arkitektur

  Vår applikation har två sorters användare: dels vår klient, som behöver kunna
  skapa animationer etc., och dels vanliga personer som ansluter via en
  webbläsare för att spela. För att kunna hantera flera spelare implementerar vi
  ett kösystem, då det inte går att spela flera spelomgångar samtidigt. När en
  spelare har nått längst fram i kön kommer spelaren att få se något gränssnitt
  där den kan spela själva spelet samt livevideo som visar den faktiska
  byggnaden där lamporna är installerade.

  Detta innebär att det behövs någon sorts webbserver som har som funktion att
  skicka individuella sidor till användaren, samt som hanterar kö- och
  spellogiken. Vi har bestämt oss för att använda Python tillsammans med
  webbservermjukvaran Tornado, se diskussion under Research tidigare i
  dokumentet.

  Vi behöver också någon komponent så hanterar kommunikation med de bryggor som
  i sin tur kommunicerar direkt med lamporna. Vi ansåg att det vore lämpligt att
  implementera webbkomponenten och lampkommunikationskomponenten som två
  separata servrar.

  Då vi behöver kunna visa livevideo från byggnaden kommer vi också att behöva
  kunna kommunicera med någon server som är kopplad till en kamera.  Detta är
  tänkt att ske via en streamingtjänst, exempelvis Bambuser.


### Arkitekturdiagram

  ![Komponentdiagram](https://github.com/smab/meta/raw/master/deliverable/component_diagram.png)
  ![Motsvarande i .svg-format](https://docs.google.com/file/d/0B4acd1MFyToeSkdFRmhEdWFGSkE/edit?pli=1)


## Risker

  Risk | Åtgärd | Sann. | Impact
  -----|--------|-------|----------
  Kommunikation mellan bryggor och lampor är opålitlig (väldigt stor fördröjning, tappar signaler, etc.) | Fixa eventuella buggar; Använda fler bryggor vid behov; Programmera egen brygga | Hög | Hög
  Kommunikation mellan lampservern och bryggorna är bristfällig (för långsam/opålitlig) | Fixa eventuella buggar; Fixa diverse tekniska problem med anslutning | Medel | Hög
  Lamporna stör varandra när de har olika färger (t.ex. två fönster inom samma rum) | Skärmar mellan lamporna; Begränsa så att lampor i samma rum alltid har samma färg | Låg | Medel
  Problem med ihopkopplingen av delsystem(lamp- och webbserver etc.) (interna protokoll matchar inte, inkorrekt data, etc.) | Fixa eventuella buggar | Medel | 11/10
  Webbservern och/eller webbgränssnittet är instabila | Fixa eventuella buggar | Medel | Medel
  Webbservern får fler besökare än den kan hantera (överbelastning, stort intressen, DoS) | Köra webbserver i molnet (Amazon eller liknande); Optimera koden lite; Stäng av spel och spela animation istället (ej interaktiv dock); Iptables-magi? (droppa paket) | Låg | Medel
  Osynkade animationer (lampor byter färg i varierande hastigheter så att lamporna är i osynk med varandra) | Använda fler bryggor; Begränsa animationerna så att de inte är för beroende av perfekt synk | Medel | Medel
  Webbkamerastreaming fungerar dåligt (lamporna syns dåligt, dålig bildkvalitet, laggigt, ingen bild alls, kameran ramlar ner) | Fixa eventuella buggar; Bättre Internetuppkoppling; Bättre kamera; Bättre kamerainstallation | Medel | Medel
  Huset syns dåligt i webbkameran p.g.a väderleksförhållanden eller liknande, t.ex. regn eller dimma. | [Bättre väder][1]; Stänga av Playhouse när det är dålig sikt | Låg | Låg

[1]: http://en.wikipedia.org/wiki/Weather_modification


## Dokumentation

  Dokumentation av kodbasen görs successivt under utvecklingen, så att
  framtida utvecklare kan ta över och fortsätta projektet.  Själva
  arkitekturen och installation av komponenter måste också dokumenteras.
  Dokumentation av arkitekturen finns i begränsad mån i detta dokument i
  dagsläget, men bör migreras till ett separat dokument och göras mer
  fullständig.


## Träning

  Vårt projekt involverar två sorters användare: de som installerar lamporna
  och bestämmer vad som visas, och slutanvändare som interagerar med
  installationen genom spel via en spelfrontend.  Det senare är
  förhoppningsvis intuitivt (spelarna antas känna till reglerna för tre-i-rad
  och fyra-i-rad).  Den förstnämnda gruppen behöver dock någon form av guide,
  inte minst för installationen av lampor.  Det nuvarande systemet för
  installation är temporärt; vi planerar att dokumentera uppsättningsprocessen
  när vi har fått ett bättre system på plats.  Även hur man ställer in
  animation och väljer spel bör dokumenteras, men för detta ändamål bör det
  räcka med en relativt kort hjälptext i själva gränssnittet.



---

# Appendix A: Skisser

  I detta appendix inkluderas skisser på de olika gränssnitt olika typer av
  användare kan se, som berör projektet.

## Konfiguration
  Vår idé kring hur konfiguraionsgränssnittet kunde se ut inkluderas nedan.

  ![Konfiguration](https://github.com/smab/meta/raw/master/deliverable/images/sketch-config.png)

  Det nuvarande konfigurationsgränssnittet:

  ![Konfiguration](https://github.com/smab/meta/blob/master/deliverable/sepdata1.png)

## Spel
  Vi hade tidigare flera idéer på hur spelgränssnittet kan se ut.  Skisser på
  designidéer inkluderas nedan.

  ![Spelfrontend: förslag 1](https://github.com/smab/meta/raw/master/deliverable/images/sketch-game-1.png)

  ![Spelfrontend: förslag 2](https://github.com/smab/meta/raw/master/deliverable/images/sketch-game-2.jpg)

  Det nuvarande spelgränssnittet:

  ![Spelfrontend: aktuella](https://github.com/smab/meta/blob/master/deliverable/sepdata2.png)



---

# Appendix B: Dokumentation

Nedan följer all dokumentation kring projektet.  Vi har försökt skriva
dokumentationen på engelska eftersom källkoden till projektet ligger öppet för
allmänheten och andra utomstående kan vara intresserade av att sätta upp
projektet.


## Webbserver: Konfiguration (engelska)

### Overview
The configuration interface can be reach as a webpage on `http://localhost:<config_port>/config` where the default port is `8081`.

There are six source files directly associated with this module, which can be
found in the relevant directories:

1. **`config.py`**:
   the main module source code, responsible for handling all requests in the configuration interface
2. **`config_base.html`**
   base template file
3. **`config_setup.html`**
   template file for Setup
4. **`config_game.html`**
   template file for Settings
5. **`config_bridges.html`**
   template file for Bridges
6. **`config_preview.html`**
   template file for Preview

### Configuration file
Everything under Setup and Settings can also be changed manually in `config.json`.

#### Attributes
* `game_name`
* `game_paths`
* `lampdest`
* `lampport`
* `serverport`
* `configport`
* `stream_embedcode`
* `ssl`
* `light_pwd`
* `config_pwd`

### Configuration interface
#### Setup

This page contains settings for connections and external services.
Some of settings may require that the server is restarted.

#### Connections
* **`Status`**             Show the current connection status to the lamp server.
* **`Lamp server`**        Address to the lamp server and what port to connect to. (default: `localhost:4711`)
* **`Game server port`**   This is the port the web server that serves the game interface will listen on. (default: `8080`)
* **`Config server port`** This is the port the web server that serves the configuration interface will listen on. (default: `8081`)

Note: Do not use the same port for game and config or the game interface will not be able to start.

#### Streaming
* **`Embed code`**         The content in this text area will be inserted in the game interface and is primarily for embedding a live stream player. (default: ` `)


#### Settings
This pages is used to change game and game settings.

#### Changing game
All games found in the game paths is listed to the left and the current game can be changed directly by clicking on any of the listed games.
Note: Changing game paths has to be done by editing `game_paths` in the config file.

#### Game settings
Game settings are shown on the right and will show the config template specified by `config_file` in the the running game module. For more information, see the documentation on game settings for each module.


### Bridges
This menu handles all the Hue bridges that are used. It lists all bridges the lightserver 
knows about, sorted by their MAC-address.

#### Identifying Selected 
By selecting bridges with the checkbox, you can tell the bridge to blink all the lamps 
associated with this bridge by pressing the "Identify Selected" button. 

#### Valid username 
Each Hue bridge needs a username. This acts like a password so unauthorized people cannot send 
commands to your lamps. Each bridge in the table has a property "valid_username" which tells you 
if the lightserver knows about a valid username for that bridge. By clicking the property, you can tell 
the lightserver to generate a new username. A confirmation box will appear and you will have to physically  press the link button on the bridge before accepting. 

#### Adding bridges 
You can add a new bridge by writing its IP address in the textfield and pressing "Add bridge." 

#### Removing bridges 
You can remove bridges by select them with the checkboxes and then pressing "Remove Selected." 

#### Refresh List 
A cached copy of the bridges will be saved on the webserver to decrease waiting time. If any changes happens to the bridges it will not be shown however. You can force a request for a new version by pressing the "Refresh List" button. 

#### Search Bridges 
If you know there are bridges on the same local network as the lightserver, you can have it search for them. It will do that by a broadcast message and by reading the Philips website. This search may take some time though and after about 20s you _must_ refresh the list by pressing the "Refresh List." 


### Grid

This page is used to configure the lamp positions in the grid and the dimensions of the grid.
The grid overview shows the positions where lamps are placed and the status of those lamps.

#### Color coding
* `white` no lamp placed
* `blue`  a lamp is placed here and no errors found (note: the lamp server can't know if a lamp is reachable or not)
* `red`   a lamp is placed here but there is no bridge with this lamp id

#### Placing lamps
Before placing the lamps, it is recommended to first turn off any running games. It can be done directly from the grid page by clicking on the `Turn Off`-button.

When you open the page, a lamp light up and then can you say which lamp was lit. This can be done either by clicking on the overview or manually enter the position and then click on `Place Lamp`. Attempting to place a lamp on an occupied position will instead remove the currently placed lamp on that position and queue it for placement.

#### Changing size
Changing size is done by entering the dimensions as `height`x`width` and then click `Change Size`.
Note: This will clear the grid and because of that the `Change Size`-button will be disabled to prevent loss of unsaved changes. Saving or refreshing will reenable the button.

#### Actions
* **`Save`**             Send and use the grid on the lamp server.
* **`Refresh`**          Discard the local grid and request the one currently used on the lamp server.
* **`Turn Off`**         Cancel any running game and turn off all lamps.
* **`Run Diagnostics`**  Run diagnosics to test the grid on the lamp server.

#### Errors
* `No activated lamp`  there is either no more lamps available that isn't already placed
* `Invalid position`   the position were in an incorrect format and couldn't be parsed be the server
* `Invalid size`       the size were in an incorrect format and couldn't be parsed be the server
* `Invalid lamp`       the placed lamp is no longer valid and can't be placed
* `Saving failed`      given when the lamp server couldn't save the grid



## Webbserver: GIF-animationer (engelska)

This documentation gives an overview of the GIF Animation module (`gifanimation.py`).

## Overview

The GIF Animation module is used to display animations in the Playhouse project.
It uses the widely supported `.gif` file format, from which it reads animations
and displays them on the grid of lamps in the Playhouse setup.

There are three source files directly associated with this module, which can be
found in the relevant directories:

1. **`gifanimation.py`**:
   the main module source code, responsible for all logic concerning how animations
   are read and displayed on the lamps, and is loaded into the webserver as a game.

2. **`gifanimation.html`**:
   template file specifying what is shown to visitors of the web page.

3. **`gifconfig.html`**:
   template file specifying the configuration interface.

## Technical details

* The module is based on the `lightgames.py`
  [game API](https://github.com/smab/playhouse-web/wiki/Game%20API), and is
  therefore considered a non-interactive game within the `playhouse-web` package.

* The module is implemented using the Python 3 package
  [Pillow](http://python-imaging.github.io/) for reading the image files.

* The module takes advantage of [Tornado](www.tornadoweb.org/) web server
  features to enable non-blocking looping over animations.

* Animations will be displayed starting at point (0,0) in the lamp grid, which
  is usually the top rightmost lamp, unless otherwise specified in the settings.

* Animations of any width and height will work, no matter the size of the lamp
  grid. No unecessary data will be transmitted to the lamp server.

* Frames are communicated to the lamp server one full frame at a time, to reduce
  possibility of some lamps lagging behind because of delay in network traffic.

* Animation frames are displayed on the lamps for the duration specified in
  the GIF file.


### Settings

These are the settings available for the GIF Animation module. They can be found
under **Settings** in the Playhouse config interface on the webserver, after
starting the module/game.

* **`New animation`**
Used to upload a new animation. Upload file must be of type `image/gif` and is
only stored in RAM on the server.

* **`Play animation`**
Turn on to start the animation loop, which will continously read frames from
the animation file and send the processed data to the lamp server for display.

* **`Center horizontally`**
If enabled, will center the animation on the x-axis of the lamp grid.

* **`Center vertically`**
If enabled, will center the animation on the y-axis of the lamp grid.

* **`Offset horizontally`**
Will offset the animation the specified number of lamps/pixels on the x-axis
of the lamp grid. Must be set to an integer value to have effect.

* **`Offset vertically`**
Will offset the animation the specified number of lamps/pixels on the y-axis
of the lamp grid. Must be set to an integer value to have effect.

* **`Transition time`**
Specifies the time, in tenths of a second, it will take for a lamp to fade from
the previous color to the next when switching frame. Must be set to an integer
value to have effect.

Note: The four settings concerning the placement of the image all work in
conjunction with each other and on any image size. For example: a 1x1 image on
a 3x3 grid, centered horizontally, offset horizontally by -1, and offset
vertically by 2, will display in the bottom left corner.


### The animation loop

The animation loop will when started continuously loop over the animation.
It will only stop when explicitly turned off in the settings. All other changes
will take effect somewhere in the loop.

When the animation is turned off, it will continue processing the current frame,
send it to lamp server, wait for the duration of the frame, then turn all lights off.

When the animation file is changed, the previous animation will keep playing until
the last frame, and then be exchanged for the new one. When the animation file is
changed, all lamps will also be reset.

When any of the settings concerning the placement of the image on the lamp grid is
changed, this will take effect on the next frame. This will also reset the lamps.

When the transition time is changed, this will have effect on the next frame.


## Creating animations
Animations can be created in any image editing software that can export to the
standard `.gif` file format.

The GIF Animation module will loop through each frame in order, extract the
per-pixel color values, and display them on the lamp grid for the duration
specified in the GIF file.


##### Example: GIMP ([GNU Image Manipulation Program](http://www.gimp.org/))
While there might be specialized software better suited for creating animated GIFs,
GIMP is a free and open source solution available and easily accessible on most platforms.
It has also been used to create most of the animations used for testing during development.

1. Create each frame of your animation as a layer in your image.

2. Name your layers according to the order they are to displayed in and the duration
   each frame is supposed to visible for. E.g. `Frame 1 (500 ms)`, `Frame 2 (1000 ms)`,
   `Frame 3 (500 ms)`, etc.

3. Go to `File > Save As...` or `File > Export To...` (whichever is applicable on your
   version), chose file format `GIF image (*.gif)`, specify a file name and click `Save`.

4. Check the `Save as Animation` box, and click `Export`.

5. Specify `Animated GIF options` as appropriate. `Save`. Done.


### Limitations

The GIF Animation module does not take full advantage of the GIF file format.
Listed here are some of the limitations that apply, and things that might not
work due to not having been tested.

* The **background color** attribute in GIF files is completely ignored.

* The **transparent color** attribute in GIF files is completely ignored.

* The GIF file format supports images consisting of frames each made up of
  multiple image blocks and palettes. While this should probably work, as
  Pillow claims full support for GIF images, it has not been tested. (It
  also shouldn't be any problem to do without, considering the practical
  limitations on the size of the image in a Playhouse setup.)

* In Playhouse, all GIFs are forever looping.



## Webbserver: Spel-API (engelska)

This documentation gives an overview of how to use the game API
(`lightgames.py`) in order to create a Playhouse game.

## Overview

  Creating a game consists of subclassing the `lightgames.Game` class, as well
  as creating template files for the game and its corresponding configuration.
  For a game 'yourgame', the relevant files relative to the repository root
  are detailed below.

      ─ src
        ├── games
        │   └── yourgame.py
        └── lightgames.py
      ─ static
        ├── game-base.css
        └── game-base.js
      ─ templates
        ├── config
        │   ├── baseconfig.html
        │   └── yourgame.html
        └── game
            ├── base.html
            └── yourgame.html

  The file `lightgames.py` contains most of the API functions that you will be
  interacting with, a well as the class that your game extends.  The files
  `game-base.css` and `game-base.js` contain the CSS and JavaScript code
  shared between all games, and are included by the `base.html` template.  The
  files `base.html` and `baseconfig.html` contain the base HTML outline that
  all games' templates (and their respective configuration templates) extend.
  You don't have to edit these files, but may want to inspect them to learn
  more about how they work and what functionality they provide.


## Lifetime of a game

  Your core game class, as previously mentioned, should extend the
  `lightgames.Game` class.  The actual game logic is implemented by overriding
  appropriate methods invoked by the rest of the game infrastructure (i.e. the
  webserver) when appropriate events happen.  This section documents what
  these events are, and when they are called.

  The `Game` class itself maintains a set of handlers corresponding to
  connected clients, so that each game doesn't have to do that manually.


### Setup & undoing setup
  * **`init(self)`**  
    When the game instance is instantiated, its `init` method is invoked.  Add
    initialization code for setting up a game instance here.  The default
    implementation provided by the `Game` class simply invokes `reset`.

  * **`reset(self)`**  
    Each time the state of a game object should be reset, its `reset` method
    is invoked.  Note that the same instance is re-used for multiple game
    sessions.  This method is invoked after a game is completed, when options
    are changed, etc.

  * **`destroy(self)`**  
    Inovked when this game instance is about to be unloaded, and won't ever be
    re-used.  The default implementation notifies all connected users that the
    game was destroyed.

### Game implementation
  * **`on_message(self, handler, message)`**  
    This is the most important method for the purpose of implementing a game.
    Invoked each time the game receives a JSON message from a client.
    `message` is the parsed JSON message (as a Dict/List/...) object.

  * **`sync(self, handler)`**  
    The idea that this method syncs the current state of the game with the
    given client (`handler`).  See also the `sync_all` utility function.

### Metadata
  * **`set_options(self, config)`**  
    Invoked when the game options were updated, with a new configuration (as a
    dict mapping option-name keys to strings).  The game should update its
    internal state to take these new options into account, and reset the game.
    May return a string, which is then interpreted as an error message
    indicating a bad configuration.

### Class variables
  Furthermore, some class variables are defined in `lightgames.Game` that the
  game overrides in order to choose template files and template interpolation
  variables to be used when rendering the game.  These are:

  * `config_file`:
      the template file used for configuration (relative to `templates/config`)
  * `template_file`:
      the template file used for the game (relative to `templates/game`)
  * `template_vars`:
      interpolation options used for both the templates above.


## Utility functions
  The utility functions provided by the API is split into two groups: methods
  defined in the `Game` class, and static functions provided directly on the
  `lightgames` module.

### Lamp-related methods (methods on `Game`)
  * `send_lamp(self, x, y, change)`:
      perform a lamp change on a single lamp or on all lamps (see lamp API
      documentation for an explanation of `change`).

  * `send_lamp_all(self, change)`:
      perform a lamp change on all lamps.

  * `send_lamp_multi(self, changes)`:
      performs a set of changes in one batch, see a`send_lamp` above.

  * `reset_lamp_all(self)`:
      enables all lamps, but sets them to display "black", i.e. set all lamps
      to a soft-off state.  You probably want to invoke this in `init` or
      `reset` to preprae all lamps.

  * `send_lamp_animation(self, coords, change, callback=None, revert=False)`:
      performs a "line" animation by performing `change` to the lamps in
      positions `coords` one at a time in an animated fashion.  If `revert` is
      set, turn off the lamps similarly with a slight delay, to simulate
      movement.  If `callback` is given, call it after the whole animation has
      comleted.

### Utility methods (methods on `Game`)
  * `sync_all(self)`:
      sync all connected handlers by invoking `sync` on each of them.

  * `try_get_new_players(self, n)`:
      try to get `n` new players from the queue and add to the game (via
      `add_player`).

  * `get_spectators(self)`:
      generator for iterating over spectators.

### Utility functions (functions on `lightgames`)
  * `send_msg(handler, msg)`:
      send a single message to a single connected client.

  * `send_msgs(handlers, msg)`:
      send a single message to a set of clients (`handlers` is an arbitrary
      iterator).

  * `send_msgs_animation(handlers, coords, message, callback=None, revert=False)`:
      corresponds to `send_lamp_animation` but for updating a set of clients.

  * `reply_wrong_player(game, handler)`:
      complains to the given player that it shouldn't perform a move right
      now.  Defined as a utility function since it is a very common operation
      for games to need.

  * `game_over(game, winnerH, coords=set())`:
      perform a game over with the given handler `winnerH` as the winner, and
      the set of lamps `coords` as the winning lamps.  Notifies users about
      who won the game, plays a victory animation with `coords`, and then
      reset the game via `reset`.

  * `set_timeout(deadline, callback)`:
      call `callback` after delay `deadline`.  Thin wrapper around Tornado's
      `ioloop.add_timeout`.

  * `get_grid_size()`:
      returns the size of the grid as setup in configuration/as defined by
      available hardware.  Usable by games in order to adjust themselves to
      available lamps.

  * `rgb_to_xyz(r, g, b)`:
      performs conversion from the RGB to the xyZ colour space.

  * `rgb_to_hue(r, g, b)`:
      performs conversion from the RGB to the HSL colour space (but only the
      hue channel).

  * `parse_color(color)`:
      parses a hexadecimal RGB colour (i.e. '#FF0000') into a triple `(r,g,b)`.



## Webbserver: Kösystem (engelska)

This documentation gives an overview of the Queue module (`queue.py`).

## Overview

The Queue module lets visitors of the Playhouse website queue up to play the
various games in the Playhouse project.

Internally it uses a `collections.deque` to keep track of queue positions,
websockets for communication between the front end and back end, and session
cookies to keep track of connections. The websockets and session cookies are
shared with the rest of the Playhouse package, which makes it easy to hand over
connections to a game when it's their time to play.


### Communication

The Queue python module uses websockets to communicate with the javascript front
end. The messages are encoded with JSON, and there is only one type of message
in each direction, shown below. Messages are sent using the API specified in the
`lightgames.py` module.

The front end to back end message will contain two JSON attributes:

* `queueaction` which specifies what action the user want to take, possible values
   are `1` for joining the queue and `0` for leaving the queue.

* `session` which specifies which session this action belongs.

The back end to front end message will contain a single JSON attribute.

* `queuepos` which specifies wether or not the user is in the queue, and at what
   position. Possible values are `0` for not in the queue, and any positive integer
   for in the queue and at the position specified by the value.


### Usage in games

Games shouldn't interact with the queue directly, but rather use the methods
specified by the [Game API](Game API). There is only two methods in `queue.py` that
is then called by `lightgames.py` for usage in the games:

* `queue.get_first()`: Will return the the first available player in the queue. If
   the queue is empty, will return `None`.

* `queue.enqueue_callback(handler)`: Will be overridden by a game specific method
   in the game API, and called by the queue whenever a new player enqueues.


### Internal methods

These are the methods used internally in `queue.py`, some of  which are connected to
the rest of the Playhouse package.

* `on_connect(self, handler)`: Called externally when a new client connects. The queue
   will acknowledge this by sending a message over the `handler` websocket stating that
   the client is not in the queue.

* `size(self)`: Used to return the size of the internal `deque` object.

* `refresh(self)`: Will refresh the queue positions by iterating over the queue and send
   a message to each client with its current queue position.

* `on_close(self, handler)`: Called externally when a connection is closed. Will try to
   remove the connection from its list of session and then refresh the queue.

* `on_message(self, handler, msg)`: Called externally when a message from a client is sent
   over a websocket that is meant for the queue. This message will contain a queue action
   and the queue will try to either enqueue the client or remove it from the queue. If the
   client was removed from the queue it will refresh itself, and send a message to the client
   acknowledging that it is no longer in the queue. If the client was enqueued, it will send
   a message to the client with its position in the queue, and make and enqueue callback
   alerting the current game that there is a new player available.

* `get_first(self)`: As mentioned before, it will remove and return the first client in the
   queue. If the queue is empty, it will return `None`. If a client was removed, the queue
   will refresh itself and send a message to the client stating it is no longer in the queue.

* `clear(self)`: Will send a message to all enqueued clients stating they are no longer in
   the queue, and then remove all connections.

* `enqueue_callback(self, handler)`: This method is initially not defined, but will instead
   be overridden by the Game API. It is then called whenever a new client is enqueued, to
   allow the games to execute logic when there are new available players.



## Lampserver: API (svenska)

## Översikt

* [POST /lights](#post-lights)
* [POST /lights/all](#post-lightsall)
* [GET /bridges](#get-bridges)
* [POST /bridges/add](#post-bridgesadd)
* [POST /bridges/save](#post-bridgessave)
* [POST /bridges/[MAC]](#post-bridgesmac)
* [DELETE /bridges/[MAC]](#delete-bridgesmac)
* [POST /bridges/[MAC]/lampsearch](#post-bridgesmaclampsearch)
* [POST /bridges/[MAC]/adduser](#post-bridgesmacadduser)
* [POST /bridges/[MAC]/lights](#post-bridgesmaclights)
* [POST /bridges/[MAC]/lights/all](#post-bridgesmaclightsall)
* [POST /bridges/search](#post-bridgessearch)
* [GET /bridges/search](#get-bridgessearch)
* [GET /grid](#get-grid)
* [POST /grid](#post-grid)
* [POST /grid/save](#post-gridsave)
* [GET /status](#get-status)
* [POST /authenticate](#post-authenticate)

--

* JSON-API
* Standardport: 4711

* I stil med Hue-API:t
  - Olika URL:er beroende på funktion
  - POST och GET

* Nödvändiga funktioner
  - Söka efter brygga
  - Lägga till brygga manuellt
  - Lista bryggor och lampor
  - Ändra lampor


## Felmeddelanden

  * Response:

    ```json
    {
      "state":        "error",
      "errorcode":    "ERROR_CODE",
      "errormessage": "human-readable error message"
    }
    ```

### Standardfelmeddenden

   Felkod           | Meddelande | Noter
  ------------------|----------------------------------------|------
  `NOT_UNICODE`     | couldn't decode as UTF-8
  `INVALID_JSON`    | invalid JSON
  `INVALID_FORMAT`  | the JSON was in an unexpected format
  `NOT_IMPLEMENTED` | feature not implemented yet
  `NOT_LOGGED_IN` | user has not yet authenticated using /authenticate, or 'user' cookie was malformed | Endast om `require_password` är `true` i config.json

  Se https://github.com/smab/playhouse-lights/blob/master/src/errorcodes.py för
  komplett lista.

  Om inget annat anges resulterar ett lyckat anrop i svaret `{"state":
  "success"}`.


## Resurser

  Detta är en lista över de resurser och metoder som lampservern
  tillhandahåller.  API:t är inspirerat av REST.  `?` efter attributnamn
  betecknar valfritt attribut.

  Strukturer definierade nedan refereras till bland de olika resursernas in-
  och utdata.

  ```js
    <hue-state-ändring> = {
      "on?":             boolean (true/false),
      "bri?":            uint8   (0-255),
      "hue?":            uint16  (0-65535),
      "sat?":            uint8   (0-255),
      "xy?":             [0.0-1.0, 0.0-1.0],
      "ct?":             153-500,
      "alert?":          "none"/"select"/"lselect",
      "effect?":         "none"/"colorloop",
      "transitiontime?": uint16 (multipel av 100 ms, default: 4)
    }
  ```

### POST /lights
  Ändra state för lampor

  * **Request:**

    ```js
    [
      {
        "x":      x-koordinat för lampa,
        "y":      y-koordinat för lampa,
        "delay?": tid i sekunder som float (dvs t.ex 1.0 för en sekund, 0.5 för 500 ms) som servern ska vänta innan den genomför ändringen,
        "change": <hue-state-ändring>
      },
      ...
    ]
    ```

  * **Felmeddelanden:** Inga för tillfället

### POST /lights/all
  Sätt alla lampor till ett visst state.

  * **Request:** `<hue-state-ändring>`
  * **Felmeddelanden**
    - `INVALID_ATTRIBUTE`
    - `INVALID_VALUE`

### GET /bridges
  Få en lista på metadata för alla anslutna bryggor (IP, mac, etc).

  * **Request:** innehållet i request-bodyn ignoreras
  * **Response:**

    ```js
    {
      "state": success,
      "bridges": {
        [MAC]: {
          "ip":             ...,
          "username":       String (null om inget användarnamn satt),
          "valid_username": true/false,
          "lights":         int (-1 om valid_username är false)
        },
        ...
      }
    }
    ```

### POST /bridges/add
  Lägg till brygga med IP (och potentiellt användarnamn).

  * **Request:** `{"ip": ..., "username?": ...}`
  * **Response:**

    ```js
    {
      "state": "success",
      "bridges": {
        [MAC]: {
          "ip":             ...,
          "username":       String (null om inget användarnamn satt),
          "valid_username": true/false,
          "lights":         int (-1 om valid_username är false)
        }
      }
    }
    ```

  * **Felmeddelanden**
    - `BRIDGE_NOT_FOUND` -- "couldn't find a Hue bridge at given address '`{}`'"
    - `BRIDGE_ALREADY_ADDED` -- "bridge has already been added to the server"

### POST /bridges/save
  Sparar nuvarande bryggkonfiguration (IP-adresser samt brygganvändarnamn). Konfigurationen läses sedan in igen nästa gång servern startar.

  * **Request:** innehållet i request-bodyn ignoreras
  * **Response:** `{"state": "success"}`

### POST /bridges/add
  Lägg till brygga med IP (och potentiellt användarnamn).

  * **Request:** `{"ip": ..., "username?": ...}`
  * **Response:**

    ```js
    {
      "state": "success",
      "bridges": {
        [MAC]: {
          "ip":             ...,
          "username":       String (null om inget användarnamn satt),
          "valid_username": true/false,
          "lights":         int (-1 om valid_username är false)
        }
      }
    }
    ```

  * **Felmeddelanden**
    - `BRIDGE_NOT_FOUND` -- "couldn't find a Hue bridge at given address '`{}`'"
    - `BRIDGE_ALREADY_ADDED` -- "bridge has already been added to the server"

### POST /bridges/[MAC]
  Ändra inställningar för brygga (främst användarnamn).

  * **Request:** `{"username": ...}`
  * **Response:** `{"state": "success", "username": ..., "valid_username": true/false}`
  * **Felmeddelanden**
    - `NO_SUCH_MAC` -- "the server does not know of a bridge with the MAC address '`{mac}`'"

### DELETE /bridges/[MAC]
  Säg åt servern att glömma en brygga.

  * **Request:** innehållet i request-bodyn ignoreras
  * **Response:** `{"state": "success"}`
  * **Felmeddelanden**
    - `NO_SUCH_MAC`

### POST /bridges/[MAC]/lights
  Ändra lampor för individuella bryggor.

  * **Request:** `[{"light": nummer på lampan, "change": <hue-state-ändring>}, ...]`
  * **Response:** `{"state": "success"}`
  * **Felmeddelanden**
    - `NO_SUCH_MAC` -- "the server does not know of a bridge with the MAC address '`{mac}`'"

### POST /bridges/[MAC]/lights/all
  Ändra alla lampor för en enskild brygga.

  * **Request:** `<hue-state-ändring>`
  * **Response:** `{"state": "success"}`
  * **Felmeddelanden**
    - `NO_SUCH_MAC` -- "the server does not know of a bridge with the MAC address '`mac`'"

### POST /bridges/[MAC]/adduser
  Lägg till användare till brygga.

  * **Request:**

    ```js
    {
      "username": sträng med 10-40 tecken. Denna parameter är valfri, om
                  man inte har med denna parameter autogenereras en
                  slumpmässig nyckel.
    }
    ```

  * **Response:** `{"state": "success", “username”: nya användarnamnet}`

### POST /bridges/[MAC]/lampsearch
  Lägg till nya lampor till brygga. För att denna operation ska fungera måste
  länkknappen på bryggan tryckas.

  * **Request:** innehållet i request-bodyn ignoreras
  * **Response:** `{"state": "success"}`

### POST /bridges/search
  Sätt igång UPnP-discovery (asynkron). Om auto_add är true läggs de funna bryggorna också till till serverns interna brygglista (d.v.s. det är ej nödvändigt att anropa /bridges/add manuellt).

  * **Request:** `{"auto_add": boolean}`
  * **Response:** `{"state": "success"}`
  * **Felmeddelanden**
    - `CURRENTLY_SEARCHING` -- "currently searching for bridges"

### GET /bridges/search
  Hämta resultat från UPnP-discovery. om `/bridges/search` ej har anropats
  ännu kommer "bridges" att vara en tom map.

  * **Request:** innehållet i request-bodyn ignoreras
  * **Response:** `{"state": "success", "bridges": {mac1: ip1, mac2: ip2, ...}}`
  * **Felmeddelanden**
    - `CURRENTLY_SEARCHING`

### GET /grid
  Hämtar ut nuvarande lampgrid

  * **Request:** innehållet i request-bodyn ignoreras
  * **Response:**

    ```js
    {
      "state": "success",
      "width": int,
      "height": int,
      "grid": [
        [
          {"mac": String (MAC-adress för bryggan lampan är associerad med), "lamp": int (ID:t för lampan på bryggan)},
          ...
        ],
      ...
      ]
    }
    ```

### POST /grid
  Ersätter nuvarande lampgrid

  * **Request:** En tvådimensionell array som motsvarar rutnätet, se "grid"-attributet i svaret till GET /grid för format
  * **Response:** `{"state": "success"}`

### POST /grid/save
  Sparar nuvarande gridkonfiguration (varje lampa och vilken x/y-position, brygga, och lampnummer på bryggan som den är associerad med). Konfigurationen läses sedan in igen nästa gång servern startar.

  * **Request:** innehållet i request-bodyn ignoreras
  * **Response:** `{"state": "success"}`

### GET /status
  Returnerar alltid 200 OK

  * **Request:** innehållet i request-bodyn ignoreras
  * **Response:** respons-bodyn är tom

### POST /authenticate
  Returnerar, om lösenordet överensstämmer med det som listas i `config.json`, en kaka med namnen 'user' i HTTP-headerserna ('Set-Cookie'-headern) som måste skickas med i HTTP-requests ('Cookie'-headern) till övriga metoder. `username` ignoreras för tillfället, men kommer att vara innehållet i 'user'-kakan.

  * **Request:** `{"password": ..., "username": ...}`
  * **Response:** `{"state": "success"}`
  * **Felmeddelanden**
    - `AUTH_NOT_ENABLED`
    - `INVALID_PASSWORD`

