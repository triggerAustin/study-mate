#!/usr/bin/python3
""" Starts a Flash Web Application """
from app.models import storage, user
from app.api.v1.web import web
import os
from os import environ
from flask import jsonify, request, make_response, Flask, send_from_directory
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
@web.route('/student/dashboard/download_hw', methods=['GET'], strict_slashes=False)
def download_homeworks():
    """download hw files from student dashboard"""
    file_id = request.args.get('id')
    url  = f'http://localhost:5000/api/v1/get_study_material/{file_id}'
    res = requests.get(url)
    if res.status_code == 200:
        file_path = res.json().get('file_path')
        file_name = res.json().get('title')
    else:
        print(f"Error: {res.status_code} - {res.json()}")
    """ for student to download hw uploaded by trs"""
    return send_from_directory(os.path.dirname(file_path), file_name)
   # return send_from_directory(directory=os.path.dirname(file_path), path=file_name, as_attatchment=True)

# view study material route
@web.route('/student/dashboard/download_studyMaterial', methods=['GET'], strict_slashes=False)
def download_studyMaterial():
    """download hw files from student dashboard"""
    file_id = request.args.get('id')
    url  = f'http://localhost:5000/api/v1/get_quizz/{file_id}'
    res = requests.get(url)
    if res.status_code == 200:
        file_path = res.json().get('file_path')
        file_name = res.json().get('title')
    else:
        print(f"Error: {res.status_code} - {res.txt}")
    """ for student to download hw uploaded by trs"""
    return send_from_directory(os.path.dirname(file_path), file_name)
   # return send_from_directory(directory=os.path.dirname(file_path), path=file_name, as_attatchment=True)



# view study material route
@web.route('/teacher/dashboard/download_hw', methods=['GET'], strict_slashes=False)
def tr_download_homeworks():
    """download hw files from tr dashboard"""
    file_id = request.args.get('id')
    url  = f'http://localhost:5000/api/v1/get_study_material/{file_id}'
    res = requests.get(url)
    if res.status_code == 200:
        file_path = res.json().get('file_path')
        file_name = res.json().get('title')
    else:
        print(f"Error: {res.status_code} - {res.json()}")
    """ for student to download hw uploaded by trs"""
    return send_from_directory(os.path.dirname(file_path), file_name)
   # return send_from_directory(directory=os.path.dirname(file_path), path=file_name, as_attatchment=True)



if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
