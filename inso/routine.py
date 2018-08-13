import time
import datetime
import sqlite3

def get_entries(date):
	database_location = '/Users/Niklas/Desktop/Code/inso/inso/site.db'
	connect = sqlite3.connect(database_location)
	cursor = connect.cursor()
	cursor.execute("SELECT * FROM inso WHERE datum=\'{}\'".format(date))
	user = cursor.fetchall()
	return user

def get_user():
	database_location = '/Users/Niklas/Desktop/Code/inso/inso/site.db'
	connect = sqlite3.connect(database_location)
	cursor = connect.cursor()
	cursor.execute("SELECT title, email, username FROM post p, user u ON p.user_id=u.id")
	user = cursor.fetchall()
	return user

def send_mail(verfahren, entry):
	msg = Message('Neue Bekanntmachung im Verfahren {}'.format(user[0]), sender='insolvenz.app@gmail.com', recipients=user[1])
	msg.body = 'Hallo {}! Bei dem von Dir abbonierten Verfahren {} gibt es eine neue Bekanntmachung. Hier ist der Link dazu: {}'.format(user[2], user[0], entry[5])
	mail.send(msg)

def get_yesterday():
	timedelta = datetime.timedelta(days=-1)
	yesterday = datetime.date.today() + timedelta
	yesterday = datetime.date.today()
	return str(yesterday)

def routine():
	while True: 

		#time.sleep(3200)

		#yesterday = get_yesterday()
		yesterday = datetime.date.today()
		print(yesterday)

		new_entires = get_entries(yesterday)
		print(new_entires)

		user = get_user()
		print(user)

		for user in user:
			for entry in new_entires:
				if user[1] == entry[1]:
					send_mail(user, entry)
					print(verfahren)

		time.sleep(43200)
		#time.sleep(40000) 