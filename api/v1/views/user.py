#!/usr/bin/python3
"""
defines a the api endppoints for the user class
"""
from models.user import User
from models import storage_t
from api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

@app_views.route('/users', methods=['GET'], strict_slashes=False)
def get_users():
    """method to get all users data from db"""
    return make_response(jsonify({'error': "Not"}))

@app_views.route('/users/int:<user_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_users.yml', methods=['GET'])
def get_user(user_id):
    """method to get user based off of id"""

@app_views.route('', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/user/del_user.yml', methods=['DELETE'])
def del_user(user_id):
    """delete individual user based of off id"""

@app_views.route('/users/', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/post_user.yml', methods=['POST'])
def post_user():
    """method to create user to db"""

