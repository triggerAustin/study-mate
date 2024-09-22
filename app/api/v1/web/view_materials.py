#!/usr/bin/python3
""" Starts a Flash Web Application """
from app.models import storage, user
from app.api.v1.web import web
from os import environ
from flask import Flask, redirect, render_template, session, url_for, flash, jsonify
from hashlib import md5
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


# view study material route
@web.route('/student/dashboard/view_material', methods=['GET'], strict_slashes=False)
def view_material():
    # render upload pages
    # redirect if session exist
    if session:
        if session.get('role') == 'student':
            # get all the files
            url = 'http://localhost:5000/api/v1/get_quizzes'
            res = requests.get(url)

            print(res.text)
            if res.status_code == 200:
                files = res.json()
            else:
                print(f"Failed to retrieve studyMaterials: {res.status_code} - {res.text}")
            page = 'student-study-materials.html'

    return render_template(page, materials=files)


# view homework routes
@web.route('/student/dashboard/homework', methods=['GET'], strict_slashes=False)
def view_homework():
    # render homework page
    if session:
        if session.get('role') == 'student':
            # get student homework
            url = 'http://localhost:5000/api/v1/get_study_materials'
            res = requests.get(url)
            
            if res.status_code == 200:
                files = res.json()
                print(files, "sdfas")
            else:
                print(f"Failed to retrieve studyMaterials: {res.status_code} - {res.text}")
            page = 'student-homeworks.html'
        return render_template(page, materials=files)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
