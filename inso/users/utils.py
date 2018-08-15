import os
import secrets
from PIL import Image
from flask import url_for, current_app, render_template
from flask_mail import Message
from inso import mail


def save_picture(form_picture):
	random_hex = secrets.token_hex(8)
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
	
	output_size = (125, 125)
	i = Image.open(form_picture)
	i.thumbnail(output_size)
	i.save(picture_path)

	return picture_fn


def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Request', sender='insolvenz.app@gmail.com', recipients=[user.email])
	msg.body = f'''Um das Passwort zurückzusetzen, besuchen Sie bitte folgenden link:
	{url_for('users.reset_token', token=token, _external=True)}
	Sollten Sie kein neues Passwort angefordert haben, können Sie diese Email einfach ignorieren.
	'''
	msg.html = render_template('email_pw.html')
	mail.send(msg)





