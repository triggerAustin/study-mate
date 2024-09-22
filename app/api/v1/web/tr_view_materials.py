#!/usr/bin/python3
""" Starts a Flash Web Application """
from app.models import storage, user
from app.api.v1.web import web
import os
from os import environ
from flask import Flask, make_response, redirect, render_template, request, session, url_for, flash, jsonify
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
@web.route('/teacher/dashboard/upload-studyMaterials', methods=['GET'], strict_slashes=False)
def upload_material_tr():
    # render upload pages
    # redirect if session exist
    if session:
        if session.get('role') == 'teacher':
            # get all the files
            page = 'teacher-study-materials.html'
        else:
           return redirect(url_for('web.login'))
    # default if no session
        return render_template(page)

@web.route('/teacher/dashboard/upload-homeworks', methods=['GET'], strict_slashes=False)
def upload_homework_page_tr():
    # render upload pages
    # redirect if session exist
    if session:
        if session.get('role') == 'teacher':
            page = 'teacher-upload-homeworks.html'
        else:
           return redirect(url_for('web.login'))
    # default if no session
    return render_template(page)


# view homework routes
@web.route('/teacher/dashboard/upload_homework', methods=['POST'], strict_slashes=False)
def upload_homework_tr():
    """to upload homework"""
    # upload hw to db
    formData = request.form.to_dict()
    file = request.files.get('files')

    print(formData)
    if not file:
        return make_response(jsonify({'error': 'No file provided'}), 400)

    # Save the file to the specified directory
    email = session.get('email')
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads', 'teacher', email, 'homeworks')
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    file_name = file.filename
    file_path = os.path.join(UPLOAD_FOLDER, file_name)
    file.save(file_path)

    # Prepare the data to be stored in the database
    json_data = {
        'title': file_name,
        'description': formData.get('description', 'This is a sample description for the study material'),
        'file_path': file_path
    }

    # mixed up quizz and study material, this one takes in homeworks
    url = 'http://localhost:5000/api/v1/post_study_material/'  # Change to your actual endpoint URL
    response = requests.post(url, data=json.dumps(json_data),  headers={'Content-Type': 'application/json'})

    if response.status_code == 201:
        print('File uploaded successfully:', response.json())
        msg = "file uploaded successfully"
    else:
        print('Failed to upload file:', response.status_code, response.text)
        msg = "failed to upload file"

    # Response after successfully saving the file
    return make_response(jsonify({'message': msg, 'data': json_data})), response.status_code



# view homework routes
@web.route('/teacher/dashboard/student-submissions', methods=['GET'], strict_slashes=False)
def view_submissions_tr():
    """ for teacher to view all the submitted and uploaded homeworks"""
    # render homework page
    if session:
        if session.get('role') == 'teacher':
            # get student homework
            url = 'http://localhost:5000/api/v1/get_study_materials'
            res = requests.get(url)

            if res.status_code == 200:
                files = res.json()
            else:
                print(f"Failed to retrieve studyMaterials: {res.status_code} - {res.text}")
                files =""
            page = 'teacher-submissions.html'
        else:
            return redirect(url_for('web.login'))
        return render_template(page, materials=files)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)
