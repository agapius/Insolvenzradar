![](2etth5.gif)


# inso
  *hold all the core components for the running website
  *creates and saves user generated insolvenzPosts
# logic
  *working scraper for insolvenzanzeigen.de
  *have both scrapers run frequently (implement with time - Monday morning?)
  *fill database and have main page recognize successful finds
# run
  *if executed, runs the whole program
  *On sever/localhost execute: (env) python scripty_mysql.py & exit

### Coding
1. bei der abfrage ob abbonierte registernummern in der datenbank sind, muss gefragt werden ob die abbonierten registernummern im full string/ in der registernummer enthalten sind (Problemfall bsp.: 810 IN 161/12 K-1-1)
2. export clrear text passwords to environment variables! 

### Social
1. Talk to Schoch about the Wettbewerb and get contact details to secretary
2. define additional functionality

### future research
1. Win would be great for traction and and publicity
2. prevent blocking by IP rotating (https://www.scrapehero.com/how-to-rotate-proxies-and-ip-addresses-using-python-3/)
3. i want this: https://github.com/cgoldsby/LoginCritter
2. Once the Verfahren is detected, automatically generate an Email with:
  *A notice
  *Next steps
  *Prefilled relevant documents
  *Drafts of relevant emails that need to be sent
