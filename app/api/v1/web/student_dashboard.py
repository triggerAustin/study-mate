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

# Close the SQLAlchemy session at the end of the request lifecycle
@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()

# Defining a route for student dashboard
@web.route('/student/dashboard', strict_slashes=False)
def studentD():
    """render the register form"""
    if session.get('role') != 'student':
        return redirect(url_for('web.login'))
    return render_template('student-dashboard.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
