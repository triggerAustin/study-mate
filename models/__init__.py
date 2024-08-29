#!/usr/bin/python3
"""
initialize the models package
"""

from os import getenv


storage_t = getenv("STUDY_MATE_STORAGE_TYPE")

if storage_t == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
if storage:
    storage.reload()
else:
    print("Storage is not initialized")
    print(storage_t)
