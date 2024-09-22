#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from app import models
from app.models.user import User
from app.models.quizzes import Quizz
from app.models.study_material import StudyMaterial
from app.models.base_model import Base
from os import getenv
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

#pymysql.install_as_MySQLdb()

classes = {"User": User, "StudyMaterial": StudyMaterial, "Quizz": Quizz}


class DBStorage:
    """interaacts with the MySQL database"""
    __engine = None
    __session = None

    def __init__(self):
        """Instantiate a DBStorage object"""
        STUDY_MATE_MYSQL_USER = getenv('STUDY_MATE_MYSQL_USER')
        STUDY_MATE_MYSQL_PWD = getenv('STUDY_MATE_MYSQL_PWD')
        STUDY_MATE_MYSQL_HOST = getenv('STUDY_MATE_MYSQL_HOST')
        STUDY_MATE_MYSQL_DB = getenv('STUDY_MATE_MYSQL_DB')
        STUDY_MATE_ENV = getenv('STUDY_MATE_ENV')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(STUDY_MATE_MYSQL_USER,
                                             STUDY_MATE_MYSQL_PWD,
                                             STUDY_MATE_MYSQL_HOST,
                                             STUDY_MATE_MYSQL_DB))
        if STUDY_MATE_ENV == "test":
            Base.metadata.drop_all(self.__engine)
        else:
            # create all db tables
            Base.metadata.create_all(self.__engine)

        print(f"Initializing DBStorage with: user={STUDY_MATE_MYSQL_USER}, host={STUDY_MATE_MYSQL_HOST}, db={STUDY_MATE_MYSQL_DB}")

        self.__session = scoped_session(sessionmaker(bind=self.__engine))

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + obj.id
                    new_dict[key] = obj
        return (new_dict)

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def get_user_by_email(self, email):
        """ Retrieve a user by their email """
        try:
            return self.__session.query(User).filter_by(email=email).first()
        except Exception as e:
            print(f"Error retrieving user by email: {e}")
        return None

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reloads data from the database"""
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """call remove() method on the private session attribute"""
        self.__session.remove()

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if not found
        """
        if cls not in classes:
            print("sadfsdFasfdas", cls)
            return None

        all_cls = models.storage.all(classes[cls])
        for value in all_cls.values():
            if (value.id == id):
                return value

        return None

    def count(self, cls=None):
        """
        count the number of objects in storage
        """
        all_class = classes.values()

        if not cls:
            count = 0
            for clas in all_class:
                count += len(models.storage.all(clas).values())
        else:
            count = len(models.storage.all(cls).values())

        return count
