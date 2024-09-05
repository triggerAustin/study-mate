#!/usr/bin/python3
"""
defines a class for the quizz inherits from BaseModel and Base
"""
from app import models
from app.models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String, LageBinary
from sqlalchemy.orm import relationship
from hashlib import md5


class StudyMaterial(BaseModel, Base):
    """
    a class quizz that extends BaseModel class
    """
    if models.storage_t == 'db':
        __tablename__ = 'studyMaterial'
        title = Column(String(128), nullable=False)
        description = Column(String(500)
        study_material = Column(LargeBinary, nullable=False)
    else:
        title = ""
        description = ""
        study_material = ""

    def __init__(self):
        """
        constructor method for this class
        """
       super().__init__(self, *args, **kwargs)
