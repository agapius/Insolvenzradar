from flask import render_template, request, Blueprint
from inso.models import Post
from inso import routine
from flask import current_app
from threading import Thread
#from inso import routine
#import time


main = Blueprint('main', __name__)

with current_app.app_context():
	routine.routine()


@main.route("/")
@main.route("/home")
def home():
	return render_template('home.html', title='Home')

@main.route("/about")
def about():
	return render_template('about.html', title='About')

'''@main.route("/startscriptnow")
def startscriptnow():
	with current_app.app_context():
		thr = Thread(target=script, args=current_app)
		thr.start()
	return 'Hallo'''

@main.route("/startscriptnow")
def startscriptnow():
	with current_app():
		routine.routine()
	return 'Hello'