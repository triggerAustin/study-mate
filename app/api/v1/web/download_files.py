#!/usr/bin/python3
""" Starts a Flash Web Application """
from app.models import storage, user
from app.api.v1.web import web
import os
from os import environ
from flask import make_response, Flask, send_from_directory
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
    data  = requests.get_json()
    file_id = data.get('id')
    url  = 'http://localhost:5000/api/v1/get_study_material/{file_id}'
    res = requests.get(url)
    print(res)
    if res.status_code == 200:
        file_path = res.get('file_path')
    else:
        print(f"Error: {res.status_code} - {res.json()}")
    """ for student to download hw uploaded by trs"""
    print(file_path)
    return send_from_directory(file_path, file_name)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
