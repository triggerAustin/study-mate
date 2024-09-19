#!/usr/bin/python3
""" Starts a Flash Web Application """
from app.models import storage, user
from app.api.v1.web import web
from os import environ
from flask import make_response, Flask, redirect, render_template, request, session, url_for, flash, jsonify
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
@web.route('/student/dashboard/upload_homework', methods=['GET'], strict_slashes=False)
def upload_page():
    # render upload pages
    # redirect if session exist
    if session:
        if session.get('role') == 'student':
            page = 'student-upload-homeworks.html'
        else:
           return render_template('web.login')
    # default if no session
        return render_template(page)

#upload homework for student
@web.route('/student/dashboard/upload_homeworks', methods=['POST'], strict_slashes=False)
def upload_homework():
    formData = request.form.to_dict()
    print(request.files['files'])
    file = request.files['files']

    url = 'http://localhost:5000/study_material/'  # Change to your actual endpoint URL

    # Prepare the file and JSON data to be sent
    file_to_upload = {'file': open(file, 'rb')}
    json_data = {
        'title': 'Sample Study Material',
        'description': 'This is a sample description for the study material'
    }

    # Send POST request with file and JSON data
    response = requests.post(url, files=file_to_upload, data=json_data)

    # Check response status and content
    if response.status_code == 201:
        print('File uploaded successfully:', response.json())
    else:
        print('Failed to upload file:', response.status_code, response.text)

    return make_response(jsonify({'error' : 'pushed'}), 200)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
