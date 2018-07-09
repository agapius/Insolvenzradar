import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.insolvenzbekanntmachungen.de/cgi-bin/bl_suche.pl'
payload = 'Suchfunktion=uneingeschr&Absenden=Suche+starten&Bundesland=--+Alle+Bundesl%E4nder+--&Gericht=--+Alle+Insolvenzgerichte+--&Datum1=&Datum2=&Name=&Sitz=&Abteilungsnr=&Registerzeichen=--&Lfdnr=&Jahreszahl=--&Registerart=--+keine+Angabe+--&select_registergericht=&Registergericht=--+keine+Angabe+--&Registernummer=&Gegenstand=--+Alle+Bekanntmachungen+innerhalb+des+Verfahrens+--&matchesperpage=10&page=1&sortedby=Datum'

link_pattern="\('(.*?)'\)"
datum_pattern="(\d\d\d\d)-(\d\d)-(\d\d)"


with requests.Session() as s:
    s.headers={"User-Agent":"Mozilla/5.0"}
    s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
    res = s.post(URL, data = payload)
    soup = BeautifulSoup(res.text, "html.parser")
    for item in soup.select("b li a"):
        print(item.get_text(strip=True))
        datum = re.match(datum_pattern, item.get_text(strip=True))
        print(datum)
        print(item['href'])
        link = re.match(link_pattern, item['href'])
        print(link)
        print("\n")
    
