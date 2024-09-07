#!/usr/bin/python3
"""
defines a the api endppoints for the user class
"""
from app.models.user import User
from app.models import storage
from app.api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

@app_views.route('/users', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_user.yml', methods=['GET'])
def get_users():
    """method to get all users data from db"""
    all_users = storage.all(User).values()
    list_users = []
    for user in all_users:
        list_users.append(user.to_dict())
    return jsonify(list_users)

@app_views.route('/user/<int:user_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_users.yml', methods=['GET'])
def get_user(user_id):
    """method to get user based off of id"""
    user = storage.get(User, user_id)
    if not user:
        abort(404)

    return jsonify(user.to_dict())

@app_views.route('/users/get_user_by_email/<string:user_email>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/user/get_users_by_email.yml', methods=['GET'])
def get_user_by_email(user_email):
    """get user by email"""
    try:
        user = storage.get_user_by_email(user_email)
        if user:
            return jsonify({
                'id': user.id,
                'email': user.email,
                'role': user.role,
                'pCode': user.password
            })
        else:
            return jsonify({ 'email': user_email}), 404
    except Exception as e:
        return jsonify({"something":e})


@app_views.route('/user/del/user_id', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/user/del_user.yml', methods=['DELETE'])
def del_user(user_id):
    """delete individual user based of off id"""
    user = storage.get(User, user_id)
    print("getting")
    if not user:
        abort(404)

    storage.delete(user)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/users/post_user', methods=['POST'], strict_slashes=False)
@swag_from('documentation/user/post_user.yml', methods=['POST'])
def post_user():
    """method to create user to db"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    instance = User(**data)
    instance.save()
    return make_response(jsonify({"Created" : "success"}), 201)

@app_views.route('/users/<int:user_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/user/put_user.yml', methods=['PUT'])
def put_user(user_id):
    """update user"""
    user = storage.get(User, user_id)

    if not user:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'email', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(user, key, value)
    storage.save()
    return make_response(jsonify(user.to_dict()), 200) 
