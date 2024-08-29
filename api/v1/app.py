#!/usr/bin/python3
""" Flask Application """
from api.v1.views import app_views
from dotenv import load_dotenv
from models import storage
from os import environ
from os import getenv
from flask import Flask, render_template, make_response, jsonify, request
from flask_cors import CORS
from flasgger import Swagger
from flasgger.utils import swag_from
from flask_debugtoolbar import DebugToolbarExtension

load_dotenv()

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True
app.register_blueprint(app_views)
cors = CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

toolbar = DebugToolbarExtension(app)

@app.teardown_appcontext
def close_db(error):
    """closes data base connection on flask app close"""
    if storage:
        storage.close()
    else:
        print("Storage is None, cannot close")

@app.before_request
def log_request_path():
    print(f"Accessing route: {request.path}")


@app.errorhandler(404)
def not_found(error):
    """ 404 Error
    ---
    responses:
      404:
        description: a resource was not found
    """
    print("Routes available:", app.url_map)

    return make_response(jsonify({'error': "Not found"}), 404)

app.config['SWAGGER'] = {
    'title': 'AirBnB clone Restful API',
    'uiversion': 3
}

Swagger(app)


if __name__ == "__main__":
    """ Main Function """
    host = environ.get('HBNB_API_HOST')
    port = environ.get('HBNB_API_PORT')
    if not host:
        host = '0.0.0.0'
    if not port:
        port = '5000'
    app.run(host=host, port=port, debug=True, threaded=True)
