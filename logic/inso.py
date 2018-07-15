import requests
from bs4 import BeautifulSoup
import re
import MySQLdb

link_pattern = "\('(.*?)'\)"
datum_pattern = "(\d\d\d\d)-(\d\d)-(\d\d)"
gesellschaften_pattern = "(gmbh)|(ag)|(mbh)|(projektgesellschaft)|(ug)|(gesellschaft)"
regNo_pattern = "\d*((\w|.).(IN|IK).(\d+\/\d+))"
street_pattern = "(straße)|(strasse)"
pages_pattern = "(wurden).(\d+).(Treffer)"
#Fails:
regNo_fails = []
datum_fails = []
link_fails = []

URL = 'https://www.insolvenzbekanntmachungen.de/cgi-bin/bl_suche.pl'
payload = 'Suchfunktion=uneingeschr&Absenden=Suche+starten&Bundesland=--+Alle+Bundesl%E4nder+--&Gericht=--+Alle+Insolvenzgerichte+--&Datum1=&Datum2=&Name=&Sitz=&Abteilungsnr=&Registerzeichen=--&Lfdnr=&Jahreszahl=--&Registerart=--+keine+Angabe+--&select_registergericht=&Registergericht=--+keine+Angabe+--&Registernummer=&Gegenstand=--+Alle+Bekanntmachungen+innerhalb+des+Verfahrens+--&matchesperpage=10&page=1&sortedby=Datum'

def get_date(item):
	if re.match(datum_pattern, item.get_text(strip=True)):
		datum_raw_match = re.match(datum_pattern, item.get_text(strip=True))
		datum = datum_raw_match.group(0)
		return datum
	else:
		datum_fails.append(item)


def get_inhaber_ort(item):
	beschreibung_raw_match = re.split(datum_pattern, item.get_text(strip=True))	
	beschreibung = beschreibung_raw_match[4]
	text = re.split(",",beschreibung)
	if re.search(gesellschaften_pattern,text[0].lower()):
		inhaber = text[0]
		if re.search(street_pattern, text[1].strip(), re.IGNORECASE):
			ort = text[1].strip() +text[2]
		else:
			ort = text[1].strip() 
	else:
		inhaber = text[0]+text[1]
		if re.search(street_pattern, text[1].strip(), re.IGNORECASE):
			ort = text[2].strip() + text[3]
		else:	
			ort = text[2].strip()
	return inhaber, ort


def get_regNo(item):

	if re.search(regNo_pattern, item.get_text(strip=True)):
		regNo_raw_match = re.search(regNo_pattern, item.get_text(strip=True))	
		regNo = regNo_raw_match.group(0)
		return regNo
	else:
		regNo_fails.append(item.get_text(strip=True))
		return None


def get_link(item):
	if re.findall(link_pattern, item['href']):
		link_raw_match = re.findall(link_pattern, item['href'])
		link = "https://www.insolvenzbekanntmachungen.de" + link_raw_match[0]
		return link
	else:
		link_fails.append(item)
		return None


def get_metadata(item):
	datum = get_date(item)
	inhaber, ort = get_inhaber_ort(item)
	regNo = get_regNo(item)
	link = get_link(item)
	return datum, inhaber, ort, regNo, link


def get_bekanntmachung(link):
	res = s.get(link)
	soup = BeautifulSoup(res.text, "html.parser")
	#print(soup.body.prettify())


def get_data_from_page(URL, payload):
	with requests.Session() as s:
		s.headers = {"User-Agent":"Mozilla/5.0"}
		s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
		res = s.post(URL, data = payload)
		soup = BeautifulSoup(res.text, "html.parser")
		suchergebnisse = soup.select("b li a")
		data_from_page = []
		for item in suchergebnisse:
			datum, inhaber, ort, regNo, link = get_metadata(item)
			data_from_page.append((datum, inhaber, ort, regNo, link))
			#bekanntmachung = get_bekanntmachung(link)
	return data_from_page

def get_pages(URL, payload):
	with requests.Session() as s:
		s.headers = {"User-Agent":"Mozilla/5.0"}
		s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
		res = s.post(URL, data = payload)
		soup = BeautifulSoup(res.text, "html.parser")
		pages_raw_match = re.search(pages_pattern, soup.get_text())	
		pagesNo = int(pages_raw_match.group(2))
		return pagesNo


'''def save_data(data_from_page):
	for t in data_from_page:
		c.execute("INSERT SQL STATEMENT HERE")
def connect_db():
	db=_mysql.connect(host="localhost",user="root",
                  passwd="jasper123",db="inso")
	c=db.cursor()
	return c
	db.close()'''

pagesNo = get_pages(URL, payload)
page = 1

while page<=pages:
	print("This is ",page,"of ",pages)
	payload = 'Suchfunktion=uneingeschr&Absenden=Suche+starten&Bundesland=--+Alle+Bundesl%E4nder+--&Gericht=--+Alle+Insolvenzgerichte+--&Datum1=&Datum2=&Name=&Sitz=&Abteilungsnr=&Registerzeichen=--&Lfdnr=&Jahreszahl=--&Registerart=--+keine+Angabe+--&select_registergericht=&Registergericht=--+keine+Angabe+--&Registernummer=&Gegenstand=--+Alle+Bekanntmachungen+innerhalb+des+Verfahrens+--&matchesperpage=10&page='+page+'&sortedby=Datum'
	data_from_page = get_data_from_page(URL, payload)
	#save_data gets data_from_page in form of an array of tuples
	#then a function (safe_data) is called, which saves the data in a mysql database
	save_data(data_from_page)
	page = page + 1
