#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from app.api.v1.views.user import *
from app.api.v1.views.study_material import *
