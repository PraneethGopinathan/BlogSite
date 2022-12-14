import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Message
from flaskblog import mail
from flask_login import current_user


#Change Profile Picture
def save_picture(form_picture):
	del_file = current_user.img  #old profile pic to delete
	random_hex = secrets.token_hex(8) #8 bytes	
	_, f_ext = os.path.splitext(form_picture.filename)
	picture_fn = random_hex + f_ext
	picture_path = os.path.join(current_app.root_path, 'static/images', picture_fn)
	output_size = (170, 170)
	i = Image.open(form_picture)
	i.thumbnail(output_size, Image.ANTIALIAS)
	i.save(picture_path)
	os.remove(os.path.join(current_app.root_path, 'static/images', del_file))  #deleting the old profile pic after new pic is updated
	return picture_fn



#Sending password reset link as emial to the user
def send_reset_email(user):
	token = user.get_reset_token()
	msg = Message('Password Reset Request', sender='cryptocoders.tech', recipients=[user.email])
	msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_token', token=token, _external=True)}

If you did not make this request then simply ignore this email and no changes will be made.
'''
	mail.send(msg)