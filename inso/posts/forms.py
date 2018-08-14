from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired

class PostForm(FlaskForm):
	title = StringField('Verfahrensnummer', validators=[DataRequired()])
	content = TextAreaField('Beschreibung/Notizen', validators=[DataRequired()])
	submit = SubmitField('Verfahren abbonieren')