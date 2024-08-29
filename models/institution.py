#!/usr/bin/python3
"""
defines a class for the user inherits from BaseModel and Base
"""
import models
from models.base_model import BaseModel, Base
from os import getenv
import sqlalchemy
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from hashlib import md5


class Institution(BaseModel, Base):
    """
    a class institution that extends BaseModel class
    """
    if models.storage_t == 'db':
        __tablename__ = 'institution'
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
    else:
        email = ""
        password = ""
        institution_name = ""

    def __init__(self):
        """
        constructor method for this class
        """
        super().__init__(self, *args, **kwargs)

    def __setattr__(self, name, value):
        """sets a password with md5 encryption"""
        if name == "password":
            value = md5(value.encode()).hexdigest()
        super().__setattr__(name, value)
