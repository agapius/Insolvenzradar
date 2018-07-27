import sqlite3
con = sqlite3.connect('/home/jasper/documents/inso/flaskblog/site.db')
cur=con.cursor()

rowID = None
regNo = '41 IN 11/19'
datum = '2018-07-19'
inhaber = '3L Immmmo GmbH'
ort = 'Im Masch 91'
link = 'https://www.insolvenzbekanntmachungen.de/cgi-bin/bl_aufruf.pl?PHPSESSID=298ffa8bf41e7eccdbc700801024963b&datei=gerichte/ns/agosnabrueck/18/41_IN_11_18/2018_07_18__11_07_56_Entscheidungen_im_Verfahren.htm'

verfahren = (rowID, regNo, datum, inhaber, ort, link)

cur.execute("INSERT INTO inso VALUES (?,?,?,?,?,?)", verfahren)
con.commit()
con.close()

with open('failures.txt', 'w') as f:
	f.write('regNo failures:\n')
