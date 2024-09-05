#!/usr/bin/python3
""" Starts a Flash Web Application """
from app.models import storage, user
from app.api.v1.web import web
from os import environ
from flask import Flask, render_template, request, redirect, session, url_for, flash
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


@web.route('/login', methods=['GET', 'POST'], strict_slashes=False)
def login():
    """render the login form"""
    formData = request.form.to_dict()

    # user login data validation
    if request.method == 'POST':
        print("post")
        email = request.form.get('email')
        print(email)
        password = request.form.get('password')

        # query from db the specific user based on email
        response = requests.get(f'http://localhost:5000/api/v1/user/get_user_by_email', params={'email': email})
        user_data = response.json()
        if response.status_code == 200:
            user = user_data
            if user and check_password_hash(user.password, password):
                if user.role == 'student':
                    return redirect(url_for('student_dashboard'))
                elif user.role == 'teacher':
                    return redirect(url_for('teacher_dashboard'))
            else:
                print("get")
                flash("invalid Password")
        else:
            flash(user_data.get('error', 'Unknown error'))
    return render_template('login.html')


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
