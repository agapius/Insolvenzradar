import time
import datetime

# this script is constantly running. it mainy builds on the inso.py

while True:
	log = open('log.txt', 'w')
	latest_post = load_latest_post() 	        # this loads the latest bekanntmachung in the database
	updates = update_database(latest_post)		# this scrapes all bekanntmachungen after latest bekanntmachung, inserts them in database, and returns the data for analysis
	update_counter = 0

	user_verfahren = get_user_verfahren()		# looks up in the database, and returns a dictionary with key= user and value = verfahren

	for user, u_verfahren in user_verfahren:
		for verfahren in updates: 
			if verfahren[1] in u_verfahren:
				send_mail(user, verfahren)
				update_counter += 1
				log_data = 'Mail send to' + user + ',' + 'verfahren' + '' + str(datetime.datetime.now())

	time.sleep(43200) 					        # script sleeps for 24 hours