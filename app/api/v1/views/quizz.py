#!/usr/bin/python3
"""
defines a the api endppoints for the user class
"""
from app.models.quizzes import Quizz
from app.models import storage
from app.api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

@app_views.route('/get_quizzes', methods=['GET'], strict_slashes=False)
@swag_from('documentation/quizz/get_quizz.yml', methods=['GET'])
def get_quizzes():
    """method to get all quizzes data from db"""
    all_quizz = storage.all(Quizz).values()
    list_quizz = []
    print(all_quizz)
    for quizz in all_quizz:
         list_quizz.append({
            'file_path': quizz.file_path,
            'description': quizz.description,
            'title': quizz.title,
            'id': quizz.id
        })
    print(list_quizz)
    return jsonify(list_quizz)

@app_views.route('/get_quizz/<quizz_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/quizz/get_quizz.yml', methods=['GET'])
def get_quizz(quizz_id):
    """method to get quizz based off of id"""
    quizz = storage.get("Quizz", quizz_id)
    if not quizz:
        abort(404)
        res_data = {
            "id": quizz.id,
            "title": quizz.title,
            "description": quizz.description,
            "file_path": quizz.file_path
        }

    return jsonify(res_data)

@app_views.route('/quizz/<quizz_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/quizz/del_quizz.yml', methods=['DELETE'])
def del_quizz(quizz_id):
    """delete individual quizz based of off id"""
    quizz = storage.get(Quizz, quizz_id)

    if not quizz:
        abort(404)

    storage.delete(quizz)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/post_quizz/', methods=['POST'], strict_slashes=False)
@swag_from('documentation/quizz/post_quizz.yml', methods=['POST'])
def post_quizz():
    """method to create quizzes"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    instance = Quizz(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/quizz/int:<quizz_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/quizz/put_quizz.yml', methods=['PUT'])
def put_quizz(quizz_id):
    """update quizz"""
    quizz = storage.get(Quizz, quizz_id)

    if not quizz:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(quizz, key, value)
    storage.save()
    return make_response(jsonify(quizz.to_dict()), 200) 
