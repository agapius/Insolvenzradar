import requests
from bs4 import BeautifulSoup
import re

URL = 'https://www.insolvenzbekanntmachungen.de/cgi-bin/bl_suche.pl'
payload = 'Suchfunktion=uneingeschr&Absenden=Suche+starten&Bundesland=--+Alle+Bundesl%E4nder+--&Gericht=--+Alle+Insolvenzgerichte+--&Datum1=&Datum2=&Name=&Sitz=&Abteilungsnr=&Registerzeichen=--&Lfdnr=&Jahreszahl=--&Registerart=--+keine+Angabe+--&select_registergericht=&Registergericht=--+keine+Angabe+--&Registernummer=&Gegenstand=--+Alle+Bekanntmachungen+innerhalb+des+Verfahrens+--&matchesperpage=10&page=1&sortedby=Datum'

link_pattern = "\('(.*?)'\)"
datum_pattern = "(\d\d\d\d)-(\d\d)-(\d\d)"
gesellschaften_pattern = "(gmbh)|(ag)|(mbh)|(projektgesellschaft)|(ug)|(gesellschaft)"
regNo_pattern = "\d+((\w|.).(IN|IK).(\d+\/\d+))"

#Fails:
regNo_fails = []

def get_date(item):
	datum_raw_match = re.match(datum_pattern, item.get_text(strip=True))
	datum = datum_raw_match.group(0)
	return datum

def get_inhaber_ort(item):
	beschreibung_raw_match = re.split(datum_pattern, item.get_text(strip=True))	
	beschreibung = beschreibung_raw_match[4]
	text = re.split(",",beschreibung)
	if re.match(gesellschaften_pattern,text[0].lower()):
		inhaber = text[0]
		ort = text[1]
		#typ = 
	else:
		inhaber = text[0]+text[1]
		ort = text[2]
	return inhaber, ort


def get_regNo(item):
	if re.match(regNo_pattern, item.get_text(strip=True)):
		regNo_raw_match = re.match(regNo_pattern, item.get_text(strip=True))	
		regNo = regNo_raw_match.group(0)
		return regNo
	else:
		regNo_fails.append(item.get_text(strip=True))
		return None


def get_link(item):
	link_raw_match = re.findall(link_pattern, item['href'])
	link = "https://www.insolvenzbekanntmachungen.de" + link_raw_match[0]
	return link


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

with requests.Session() as s:
	s.headers = {"User-Agent":"Mozilla/5.0"}
	s.headers.update({'Content-Type': 'application/x-www-form-urlencoded'})
	res = s.post(URL, data = payload)
	soup = BeautifulSoup(res.text, "html.parser")
	suchergebnisse = soup.select("b li a")
	for item in suchergebnisse:
		datum, inhaber, ort, regNo, link = get_metadata(item)
		bekanntmachung = get_bekanntmachung(link)

		print(datum)
		print(inhaber)
		print(ort)
		print(regNo)
		print(link)
		print("\n")
	print("\n")
x
