from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from flask_login import current_user
from inso.models import User


class RegistrationForm(FlaskForm):
	username = StringField('Benutzername',
						   validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	password = PasswordField('Passwort', validators=[DataRequired()])
	confirm_password = PasswordField('Passwort bestätigen',
									 validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Anmelden')

	def validate_username(self, username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('Dieser Benutzername ist leider schon vergeben. Bitte wählen Sie einen anderen.')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('Diese Email ist bereits vergeben. Bitte wählen Sie eine andere.')


class LoginForm(FlaskForm):
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	password = PasswordField('Passwort', validators=[DataRequired()])
	remember = BooleanField('Angemeldet bleiben')
	submit = SubmitField('Anmelden')


class UpdateAccountForm(FlaskForm):
	username = StringField('Benutzername',
						   validators=[DataRequired(), Length(min=2, max=20)])
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	picture = FileField('Neues Profilfoto', validators=[FileAllowed(['jpg', 'png'])])
	submit = SubmitField('Update')

	def validate_username(self, username):
		if username.data != current_user.username:
			user = User.query.filter_by(username=username.data).first()
			if user:
				raise ValidationError('Dieser Benutzername ist bereits vergeben. Bitte wählen Sie einen anderen.')

	def validate_email(self, email):
		if email.data != current_user.email:
			user = User.query.filter_by(email=email.data).first()
			if user:
				raise ValidationError('Diese Email ist bereits im System. Bitte wählen Sie eine andere.')

class RequestResetForm(FlaskForm):
	email = StringField('Email',
						validators=[DataRequired(), Email()])
	submit = SubmitField('Neues Passwort anfordern')

	def validate_email(self, email):
		user = User.query.filter_by(email=email.data).first()
		if user is None:
			raise ValidationError('Wir haben keinen Account mit dieser E-mail. Sie müssen sich zunächst registrieren')


class ResetPasswordForm(FlaskForm):
	password = PasswordField('Passwort', validators=[DataRequired()])
	confirm_password = PasswordField('Passwort bestätigen',
									 validators=[DataRequired(), EqualTo('password')])
	submit = SubmitField('Passwort zurücksetzen')