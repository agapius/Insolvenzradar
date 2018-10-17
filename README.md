# Insolvenzradar

![alt text](https://imgur.com/a/4hwrEhF)

Auf www.insolvenzbekanntmachungen.de veröffentlichen die Insolvenzgerichte Bekanntmachungen in Insolvenzverfahren. Diese öffentliche Bekanntmachung erfolgt gemäß § 9 Abs. 1 InsO und setzt die zweiwöchige Beschwerdefrist in Gang. Insolvenzverwalter oder rechtlicher Vertreter in einem Insolvenzverfahren müssen die Website also regelmäßig (mindestens einmal pro Woche) hinsichtlich aller betreuter Verfahren überprüfen. Dies geschieht in vielen Kanzleien durch eine Sekretärin oder einen wissenschaftlichen Mitarbeiter.   
Der Insolvenzradar (abrufbar unter www.q-labs.io) nimmt diese Arbeit komplett ab. Die betreuten Verfahren werden einmal eingegeben. Danach werden täglich alle neuen Bekanntmachungen geprüft und der Benutzer wird E-mail benachrichtigt, sobald es eine Bekanntmachung für eines der abonnierten Verfahren gibt.  

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
