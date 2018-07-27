import requests
from bs4 import BeautifulSoup
import re
import sqlite3

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

database_location = '/home/jasper/documents/inso/flaskblog/site.db'
URL = 'https://www.insolvenzbekanntmachungen.de/cgi-bin/bl_suche.pl'
payload = 'Suchfunktion=uneingeschr&Absenden=Suche+starten&Bundesland=--+Alle+Bundesl%E4nder+--&Gericht=--+Alle+Insolvenzgerichte+--&Datum1=&Datum2=&Name=&Sitz=&Abteilungsnr=&Registerzeichen=--&Lfdnr=&Jahreszahl=--&Registerart=--+keine+Angabe+--&select_registergericht=&Registergericht=--+keine+Angabe+--&Registernummer=&Gegenstand=--+Alle+Bekanntmachungen+innerhalb+des+Verfahrens+--&matchesperpage=10&page=1&sortedby=Datum'


def get_date(item):
	if re.match(datum_pattern, item.get_text(strip=True)):
		datum_raw_match = re.match(datum_pattern, item.get_text(strip=True))
		datum = datum_raw_match.group(0)
		return datum
	else:
		datum_fails.append(item)


def get_ort(item):
	beschreibung_raw_match = re.split(datum_pattern, item.get_text(strip=True))	
	beschreibung = beschreibung_raw_match[4]
	text = re.split(",",beschreibung)
	if re.search(gesellschaften_pattern, text[0].lower()):
		if re.search(street_pattern, text[1].strip(), re.IGNORECASE):
			ort = text[1].strip() +text[2]
		else:
			ort = text[1].strip() 
	else:
		if re.search(street_pattern, text[1].strip(), re.IGNORECASE):
			ort = text[2].strip() + text[3]
		else:	
			ort = text[2].strip()
	return ort


def get_inhaber(item):
	beschreibung_raw_match = re.split(datum_pattern, item.get_text(strip=True))	
	beschreibung = beschreibung_raw_match[4]
	text = re.split(",",beschreibung)
	if re.search(gesellschaften_pattern,text[0].lower()):
		inhaber = text[0]
	else:
		inhaber = text[0]+text[1]
	return inhaber


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
	inhaber = get_inhaber(item)
	ort = get_ort(item)
	regNo = get_regNo(item)
	link = get_link(item)
	return datum, inhaber, ort, regNo, link


def get_bekanntmachung(link):
	res = s.get(link)
	soup = BeautifulSoup(res.text, "html.parser")
	return soup.body.prettify()


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
			rowID = None
			data_from_page.append((rowID, regNo, datum, inhaber, ort, link))
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

def insert_into_database(database_location, data_from_page):
	con = sqlite3.connect(database_location)
	cur= con.cursor()
	for verfahren in data_from_page:
		cur.execute("INSERT INTO inso VALUES (?,?,?,?,?,?)", verfahren)
		con.commit()
	con.close()
'''
def save_data(data_from_page):
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

while page<=pagesNo:
	print("This is ",page,"of ",pagesNo)
	percent = page/507*100
	print("we are ", percent ,"Percent done.")
	payload = 'Suchfunktion=uneingeschr&Absenden=Suche+starten&Bundesland=--+Alle+Bundesl%E4nder+--&Gericht=--+Alle+Insolvenzgerichte+--&Datum1=&Datum2=&Name=&Sitz=&Abteilungsnr=&Registerzeichen=--&Lfdnr=&Jahreszahl=--&Registerart=--+keine+Angabe+--&select_registergericht=&Registergericht=--+keine+Angabe+--&Registernummer=&Gegenstand=--+Alle+Bekanntmachungen+innerhalb+des+Verfahrens+--&matchesperpage=100&page='+str(page)+'&sortedby=Datum'

	data_from_page = get_data_from_page(URL, payload)
	#save_data gets data_from_page in form of an array of tuples
	insert_into_database(database_location, data_from_page)
	#then a function (safe_data) is called, which saves the data in a mysql database
	page = page + 1

print("Finished crawling!!!")

#print failures to txt
with open('failures.txt', 'w') as f:
	f.write('regNo failures:\n')
	for failure in regNo_fails:
		f.write(failure)

	f.write('\n')
	f.write('datum failures:\n')
	for failure in datum_fails:
		f.write(failure)

	f.write('\n')
	f.write('link failures:\n')
	for failure in link_fails:
		f.write(failure)
f.closed

