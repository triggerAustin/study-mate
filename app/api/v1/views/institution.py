#!/usr/bin/python3
"""
defines a the api endppoints for the user class
"""
from app.models.institution import Institution
from app.models import storage
from app.api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

@app_views.route('/institution', methods=['GET'], strict_slashes=False)
@swag_from('documentation/institution/get_institution.yml', methods=['GET'])
def get_institution():
    """method to get all institution data from db"""
    all_institution = storage.all(Institution).values()
    list_institution = []
    for institution in all_institution:
        list_institution.append(institution.to_dict())
    return jsonify(list_institution)

@app_views.route('/institution/int:<institution_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/institution/get_institution.yml', methods=['GET'])
def get_institution(institution_id):
    """method to get institution based off of id"""
    institution = storage.get(Institution, institution_id)
    if not institution:
        abort(404)

    return jsonify(institution.to_dict())

@app_views.route('/institution/int:<institution_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/institution/del_institution.yml', methods=['DELETE'])
def del_institution(institution_id):
    """delete individual institution based of off id"""
    institution = storage.get(Institution, institution_id)

    if not institution:
        abort(404)

    storage.delete(institution)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/institution/', methods=['POST'], strict_slashes=False)
@swag_from('documentation/institution/post_institution.yml', methods=['POST'])
def post_institution():
    """method to create institution"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    if 'email' not in request.get_json():
        abort(400, description="Missing email")
    if 'password' not in request.get_json():
        abort(400, description="Missing password")

    data = request.get_json()
    instance = Institution(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/institution/int:<institution_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/institution/put_institution.yml', methods=['PUT'])
def put_institution(institution_id):
    """update institution"""
    institution = storage.get(Institution, institution_id)

    if not institution:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'email', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(institution, key, value)
    storage.save()
    return make_response(jsonify(institution.to_dict()), 200) 
