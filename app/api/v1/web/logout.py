#!/usr/bin/python3
""" Starts a Flash Web Application """
from app.api.v1.web import web
from os import environ
from flask import Flask, redirect, session, url_for

app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


# Close the SQLAlchemy session at the end of the request lifecycle
@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


# Define the logout route
@web.route('/logout', methods=['GET'], strict_slashes=False)
def logout():
    """logout user"""
    session.clear()  # This will remove all session data
    return redirect(url_for('web.login'))


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
