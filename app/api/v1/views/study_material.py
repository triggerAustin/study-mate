#!/usr/bin/python3
"""
defines a the api endppoints for the user class
"""
from app.models.study_material import StudyMaterial
from app.models import storage
from app.api.v1.views import app_views
from flask import abort, jsonify, make_response, request
from flasgger.utils import swag_from

@app_views.route('/study_material', methods=['GET'], strict_slashes=False)
@swag_from('documentation/study_material/get_study_material.yml', methods=['GET'])
def get_study_material():
    """method to get all study_material data from db"""
    all_study_material = storage.all(StudyMaterial).values()
    list_study_material = []
    for material in all_study_material:
        list_study_material.append(material.to_dict())
    return jsonify(list_study_material)

@app_views.route('/study_material/int:<material_id>', methods=['GET'], strict_slashes=False)
@swag_from('documentation/quizz/get_material.yml', methods=['GET'])
def get_study_material(material_id):
    """method to get material based off of id"""
    material = storage.get(StudyMaterial, material_id)
    if not material:
        abort(404)

    return jsonify(material.to_dict())

@app_views.route('/study_material/int:<material_id>', methods=['DELETE'], strict_slashes=False)
@swag_from('documentation/study_material/del_study_material.yml', methods=['DELETE'])
def del_study_material(material_id):
    """delete individual material based of off id"""
    material = storage.get(StudyMaterial, material_id)

    if not material:
        abort(404)

    storage.delete(material)
    storage.save()

    return make_response(jsonify({}), 200)

@app_views.route('/study_material/', methods=['POST'], strict_slashes=False)
@swag_from('documentation/study_material/post_study_material.yml', methods=['POST'])
def post_study_material():
    """method to create study_material"""
    if not request.get_json():
        abort(400, description="Not a JSON")

    data = request.get_json()
    instance = StudyMaterial(**data)
    instance.save()
    return make_response(jsonify(instance.to_dict()), 201)

@app_views.route('/study_material/int:<material_id>', methods=['PUT'], strict_slashes=False)
@swag_from('documentation/study_material/put_study_material.yml', methods=['PUT'])
def put_study_material(material_id):
    """update study_material"""
    material = storage.get(StudyMaterial, material_id)

    if not material:
        abort(404)

    if not request.get_json():
        abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']

    data = request.get_json()
    for key, value in data.items():
        if key not in ignore:
            setattr(material, key, value)
    storage.save()
    return make_response(jsonify(material.to_dict()), 200) 
