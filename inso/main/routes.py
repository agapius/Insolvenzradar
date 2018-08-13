from flask import render_template, request, Blueprint
from inso.models import Post
from inso import routine
import time


main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
	return render_template('home.html', title='Home')

@main.route("/about")
def about():
	return render_template('about.html', title='About')

time.sleep(20)
routine.routine()
