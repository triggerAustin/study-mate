#!/usr/bin/python3
""" Starts a Flash Web Application """
from flask import Flask, jsonify
from flask_mail import Mail, Message
from .config import MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD, MAIL_USE_TLS, MAIL_USE_SSL
from . import web

app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True

# Apply configuration settings to Flask app
app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_USE_TLS'] = MAIL_USE_TLS
app.config['MAIL_USE_SSL'] = MAIL_USE_SSL


mail = Mail(app)

@web.route('/send_email/<email>', methods=['POST'], strict_slashes=False)
def send_email(email):
    subject = 'Hello from Flask'
    body = 'This is a test email sent from a Flask application.'

    msg = Message(subject, sender=MAIL_USERNAME, recipients=[email])
    msg.body = body
    try:
        mail.send(msg)
        return jsonify({"message": "Email sent successfully!"}), 200
    except Exception as e:
        return jsonify({"message": str(e)}), 500



if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
