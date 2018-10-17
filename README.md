# Insolvenzradar

Auf www.insolvenzbekanntmachungen.de veröffentlichen die Insolvenzgerichte Bekanntmachungen in Insolvenzverfahren. Diese öffentliche Bekanntmachung erfolgt gemäß § 9 Abs. 1 InsO und setzt die zweiwöchige Beschwerdefrist in Gang. Insolvenzverwalter oder rechtlicher Vertreter in einem Insolvenzverfahren müssen die Website also regelmäßig (mindestens einmal pro Woche) hinsichtlich aller betreuter Verfahren überprüfen. Dies geschieht in vielen Kanzleien durch eine Sekretärin oder einen wissenschaftlichen Mitarbeiter.   

Der Insolvenzradar (abrufbar unter www.q-labs.io) nimmt diese Arbeit komplett ab. Die betreuten Verfahren werden einmal eingegeben. Danach werden täglich alle neuen Bekanntmachungen geprüft und der Benutzer wird E-mail benachrichtigt, sobald es eine Bekanntmachung für eines der abonnierten Verfahren gibt.  


<img src="https://im.ezgif.com/tmp/ezgif-1-edc49e5bee74.gif">


# Technical Components:

## inso
  *hold all the core components for the running website
  *Register new User, Login, Forgotten Password, Overview Page
  *creates and saves user generated insolvenzPosts in a MySQL Database
## logic
  *working scraper for insolvenzbekanntmachungen.de
  *runs daily - time is flexible
  *fills MySQL database with all new Publications 
  *recognizes if there are new publications, users have subscribed to
  *sends user an email, that there is a new publication
## run
  *if executed, runs the whole program
  *On sever/localhost execute: (env) python scripty_mysql.py & exit

# Todo:

## Coding
1. Stop running page in Developer Mode
2. export clear text passwords for email client to environment variables! 
3. define additional functionality

### future research
1. prevent blocking by IP rotating (https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/)
2. More relevant Email with:
  *Next steps
  *Prefilled relevant documents
  *Drafts of relevant emails that need to be sent

## Größere Vision 

### Insolvezradar als Teil eines Programm zur Modellierung von Unternehmen:

1. **Modellierung:**
Wir bauen ein ER Modell für Juristische Personen (Klassen) mit unterklassen von einzelnen (BGB-Gesellschaft, GmbH, AG) und deren verbindungen (gehört) (wird geleitet von) Personen (mitarbeiter, Geschäftsführer). Dazu sourcen wir zunächst Informationen (siehe Datenschnittstellen) und setzen diese dann in Relation zueinander (siehe ER/Klassen-Modell und Relation).
Ziel ist ein möglichst vollständiges Modell.

2. **Datenschnittstellen:**

  * Insolvenzradar: In Zukunft können Informationen über Insolvenzverfahren direkt durch unser Datenmodell abgerufen werden. Sobald dies eine Instanz zu einem Insolvenzverfahren erstellt (oder bei einer Gesellschaftsinstanz ein solches vermerkt) wird unsere InsoApp darüber informiert und hält Ausschau nach entsprechenden Bekanntmachungen. Diese werden sofort an das Datenmodell zurückgemeldet und an der entsprechenden Stelle vermerkt und abrufbar gemacht. Der Anwalt hat so innerhalb kürzester Zeit und ohne ein Finger gerührt zu haben ein Überblick über den Verfahrensstand. 

  * Datenräume: Analyse von großen juristischen Dokumentenmengen, insbesondere von Dokumenten in Datenräumen. Sämtliche Dokumente sollen erfasst werden, deren Inhalte analysieren und in ein virtuelles Modell überführt werde. 

  * Handelsregister
  * Bekanntmachungen

3. **ER/Klassen-Modell und Relation**


### Möglichkeiten modellierter Unternehmen:
	
#### Beispiel:

_Die Mandantin besteht aus einer AG, die Gesellschafterin von zehn GmbHs ist, die jeweils Grundstücke in einer deutschen Großstadt besitzen. Die Mandantin stellt ihrem Anwalt einen Datenraum zur Verfügung, der hunderte PDFs umfasst, u.A. Kaufverträge, Vollmachten, Arbeitsverträge etc. Zunächst würde der Anwalt alle Dokumente in unser Programm einspeisen. Dieses würde dann für jede juristische Person eine Instanz kreieren, in der juristische Informationen zu dieser gesammelt werden. Wenn die A-GmbH ein Miethaus in Hamburg besitzt, und Albert Adler als Geschäftsführer besitzt, würden sowohl für die A-GmbH als auch für Albert Adler eine Instanz erstellt werden. Ein Teil des Programms würde sich Informationen aus dem Handelsregister holen und diese mit den gespeicherten Informationen vergleichen. Wenn sich unter den Dokumenten z.B. eine Vollmacht von Albert Adler im Namen der A-GmbH vom 1.1.2010 befindet, ausgestellt an Hubertus Hallenbach, würde das Programm checken, ob Adler am 1.1.2010 schon zum Geschäftsführer bestellt wurde. Falls nicht, würde es dies dem Anwalt mitteilen._

#### Vorteile:

  * **Überblick:** Aus einer Vielzahl von detaillierten Dokumenten kann ein juristisches Gesamtbild der Konzern/Transaktionsstruktur erstellt werden. So kann eine Übersicht über die Dokumente und deren Inhalte einfach erstellt werden und somit Zeit einsparen. Auch grafische Übersichten der Firmenstruktur erstellt werden (man kann bis ins kleinste detail hineinzoomen und auch wieder herauszoomen)
  _Im Beispiel hätte der Mandant hätte nun zunächst die Möglichkeit, sich die Informationen auf eine für ihn beliebige Art auszulesen. Er könnte zum Beispiel alle Informationen über die A-GmbH geordnet ausgeben, und die jeweiligen Quellen durch einen kurzen Klick öffnen. Er könnte sich auch ein Organigramm über die Konzernstruktur ausgeben lassen._

  * **Adjustierung der relevanten Dokumente:** Bei gewünschten juristischen Änderung kann der Workflow des Anwalts beschleunigen. So können Gesellschaftsverträge, Prokuras, Gesellschafterwechsel, Lieferverträge automatisch geschwärzt/angepasst werden.
  _Falls nun gewünscht ist, dass die Anteile der A-GmbH an einen Dritten übertragen werden, kann dies dem Programm mitgeteilt werden. Es würde alle Dokumente in dem Datenraum überprüfen, ob diese verändert werden müssen und dem Anwalt entsprechend eine Vorlage mit den entsprechenden Informationen vorlegen._

  * **Übeprüfung und Augmentierung der Daten:** Die Informationen können automatisch überprüft werden:
  _Die Daten aus den Dokumenten ist aber nur eine Quelle, von der unsere Programm Informationen sourcen kann. Durch andere APIs sollen automatisch weitere relevante Informationen geholt werden, zum Beispiel aus dem Handelsregister. Eine entsprechende Entwicklungs-API haben wir bereits. Hier kommt auch der zweite Teil unseres Beitrags ins Spiel: die InsoApp_

## Zukunft:

### Akkuratere Modellierung:

  * **Teilrechtsgebiete:** In einem zweiten Schritt können wir auch teilrechtsgebiete modellieren. So können wir modelle (klassen) für share/equity deal erstellen. Darüber hinaus können wir steuerrechtsklassen erstellen insbesondere wenn wir mit steurerrelationen die einzelnen   Entitäten mit dem staat verbinden, können wir sogar je nach ausgeklügeltheit der steuerklassen auch verschiedene Anteilsszenarios erstellen (also anteile herumschieben) und deren steuerrechliche implikationen sehen (Faktisch können wir   sogar unendlich zusammensetzungen modellieren und auf diese weise optimieren_

  * **Teilrechtsgebiete:** Insbesondere (ich habe mich darüber einmal in london auf super hohem niveau mit einem der meistgefundeten PE leute unterhalten) kann man unternehmen modellieren und direkt auf reale Unternehmensdaten zugreifen und so auch für Käufer besser das Unternehmen und dessen kennzahlen aufbereiten. Theoretisch genau das, was jetzt investmentbanker händisch zusammentragen (harte zahlen des unternehmens) und dann durch ihre excel-Modelle jagen. Das kann mehr und mehr direkt abgefragt werden und dann direkt in die excel modelle gepiped werden.

### Modell als neue Art über Unternehmen zu denken

  * **Höherer Zweck der Modellierung:** Datenraum-projekt ist eigentlich nur Mittel zum Zweck um an die unternehmensdaten zu kommen. Viel interessanter wäre es, wenn das unternehmen eine klasse(tabelle im folgenden klasse) AN und darin ein Objekt AN hätte und zusätzlich als unterklasse von untenehmen und rechtsform ein Unternehmensobjekt, und zusätzlich in der Relationstyp Klasse noch eine Relation zwischend dem Arbeitnehmer und dem Unternehmen mit den Attributen Arbeitsvertrag, Versicherungs, Sozialabgaben, zwischenfälle etc. Inkl. Funktionen wie kündigen, bonus, etc. 
  In dieser Datenstruktur liegt ein fundermentaler mehrwert insofern, dass nicht mehr nur noch daten geordnet gespeichert sind und menschen die relationen auf dem schirm haben müssen, sondern die Daten inklusive Relationen gespeichert sind und somit auf all diese informationen zugegriffen werden kann. 
  Darüber hinaus wird die datenstruktur immer potenter, je mehr Information hineinfließt - bis die datenstruktur ein beinahe vollständiges Modell der Realität wird und in echtzeit durch daten aus der außenwelt geupdated wird (bessere sensorik, web 4.0, smart watches für location/Urlaub/arbeitszeiten, krankheiten) und auch durch funktionen mit der außenwelt interagiert (Funktion der kündigung verschickt diese automatisch an AN und AG, so dass diese nur noch unterschreiben müssen - außerdem wird das ganze direkt in quartalsbericht geändert und bei der steuererklärung etc.) So wird das Modell immer mächtiger. 


  * **Model matures:** Modell bildet nicht mehr ab, sondern ist - erwächst zu seiner selbst: _The vision is, that eventually we won't improve the model by feeding it more and more data to make it more accurate, but that the model will mature to become the object of contemplation itself._ 
  So kulminiert eine Unternehmensdatenstruktur,die vollständig das Unternehmen und seiner Beziehungen in sich sowie zur Ausßenwelt abbildet. So können zb auch steuern als beziehungen einbezogen sein und es können abspaltungen einzelner teile in teilGmbH's modelliert werden. Das Modell gibt dann aufschluss darüber, ob das steuerlich sinnvoll ist und kann direkt die arbeitsverträge, mietverträge, etc beziehungen der beteiligten anpassen. Gleichermaßen können Übernahmen (M&A) quasi vollautomatisch gestaltet und durchgeführt werden
  Ultimativ führt das natürlich zu einem super potenten Modell, das quasi von alleine funktioniert, so kann es in echtzeit seine beziehungen überwachen und potenziell von alleine gwisse (Steuer-)optimierungen vorschlagen. Insobesondere kann es effizient oder wenigstens effektiver als ein mensch die verschiedenen Modellierungen austesten. So kann ein Mensch bei einer Menge von 3 Unternehmen noch einfach die möglichen verbindungen (Potenzmenge = 2^n = 8) ausprobieren. Bereits bei 7 Unternehmen im Verbund sind jedoch die verschiedenen möglichen Verbindungen (Potenzmenge = 2^7 = 128) schwierig einzeln durchzuspielen. Dazu kommen dann noch variationen der verbindungen (zb jedesmal gmbh, bgb gesellschaft mutter/tochter,...). Das Modell kann jedoch auch bei großen Unternehmensstrukturen alle (mit heuristiken die vielversprechendsten) Verbindungen durchspielen und so von alleine feststellen,dass nun eine AG besser als eine GmbH wäre und sämtliche prerequisiten treffen. Außerdem kann es bei z.B. immobilienprojekten vorschlagen, dass einzelimmos in einzelgmbhs abgespaltet werdn sollten. Letztlich endet die Vision in einem Modell, das aufhört einen realen Prozess zu spiegeln (Modell), sondern selber der reale Prozess zu sein.
