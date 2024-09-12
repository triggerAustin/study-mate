#!/usr/bin/python3
""" Starts a Flash Web Application """
from app.models import storage
from app.api.v1.web import web
from os import environ
from flask import Flask, render_template, redirect, url_for, session
import uuid
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@web.route('/student/dashboard', strict_slashes=False)
def studentD():
    """render the register form"""
    if session.get('role') != 'student':
        return redirect(url_for('web.login'))
    return render_template('student-dashboard.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
