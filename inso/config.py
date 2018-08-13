import os

class Config:
	SECRET_KEY = '7a4af642e0eec14ef9d49bdf833f9091'
	SQLALCHEMY_DATABASE_URI = 'mysql://inso:1nsovenzrecht@localhost/insodata'
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = 'insolvenz.app@gmail.com'
	MAIL_PASSWORD = 'insolvenz'

#move values to environment variable
# 'insolvenz.app@gmail.com'
#'insolvenz'
#7a4af642e0eec14ef9d49bdf833f9091
#sqlite:///site.db
