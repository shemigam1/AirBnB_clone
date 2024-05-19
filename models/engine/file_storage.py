#!/usr/bin/bash

"""
this module contains class FileStorage
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    """
    class Filestorage
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns dict __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets values for __objects"""
        obj_class_name = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(obj_class_name, obj.id)] = obj

    def save(self):
        """serializes __objects to __file_path"""
        with open(FileStorage.__file_path, "w") as write_to:
            obj_dicts = FileStorage.__objects.copy()
            for k in obj_dicts:
                obj_dicts[k] = obj_dicts[k].to_dict()
            json.dump(obj_dicts, write_to)

    def reload(self):
        """deserializes JSON in __file_path to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as read_from:
                data = json.load(read_from)
                # print(type(data))
                for item in data.values():
                    class_name = item['__class__']
                    del item['__class__']
                    self.new(eval(class_name)(**item))
        except FileNotFoundError:
            # print("file not found")
            return
