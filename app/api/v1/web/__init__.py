#!/usr/bin/python3
""" Blueprint for API """
from flask import Blueprint
import os
import importlib.util

web = Blueprint('web', __name__, url_prefix='/studyMate')

#current_dir = os.path.dirname(__file__)

#spec = importlib.util.spec_from_file_location("register",
#                                              os.path.join(current_dir, 'register.py'))

#hbnb_module_0 = importlib.util.module_from_spec(spec)
#spec.loader.exec_module(hbnb_module_0)
from app.api.v1.web.download_files import *
from app.api.v1.web.index import index
from app.api.v1.web.login import login
from app.api.v1.web.logout import logout
from app.api.v1.web.register import register
from app.api.v1.web.student_dashboard import studentD
from app.api.v1.web.teacher_dashboard import teacherD
from app.api.v1.web.tr_view_materials import *
from app.api.v1.web.upload import upload_homework
from app.api.v1.web.view_materials import *
print("route loaded")
