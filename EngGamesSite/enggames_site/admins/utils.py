from flask import url_for
from flask_mail import Message

from enggames_site import mail, bcrypt


def reset_password_email(admin):
    token = admin.get_reset_token()
    message = Message()
    message.subject = 'Reset Exec Password Request'
    message.sender = 'delispeter19@gmail.com'
    message.recipients = [admin.email]
    # external will provide external url
    message.body = f'''Click the following link to reset your password: 
{url_for('admins.reset_token', token=token, _external=True)}

Ignore this email to make no changes.
    '''
    mail.send(message)


def hashpassword(password):
    return bcrypt.generate_password_hash(password).decode('utf-8')