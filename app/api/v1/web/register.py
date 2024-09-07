#!/usr/bin/python3
""" Starts a Flash Web Application """
from app.models import storage, user
from app.api.v1.web import web
from os import environ
from flask import Flask, render_template, request, redirect, session, url_for, flash, jsonify, abort
import requests
import uuid
from werkzeug.security import check_password_hash
import json

app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@web.route('/register', methods=['GET', 'POST'], strict_slashes=False)
def register():
    """validate registration"""
    formData = request.form.to_dict()
    email = request.form.get('email')
    # user login data validation
    if request.method == 'POST':
        # call api to save to db
        user_exists = requests.get(f'http://localhost:5000/api/v1/users/get_user_by_email/{email}')
        if user_exists:
            return render_template('register.html', err="user exists with that email")

        response = requests.post(f'http://localhost:5000/api/v1/users/post_user/', json=formData)
        if response.status_code == 201:
            return redirect(url_for('web.login'))
        else:
            print(f"Error {response.status_code}: {response.text}")

    return render_template('register.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
