#!/usr/bin/bash

"""
this module contains class FileStorage
"""
import json
from models.base_model import BaseModel
from pathlib import Path


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
        obj_dicts = FileStorage.__objects.copy()
        for k in obj_dicts:
            obj_dicts[k] = obj_dicts[k].to_dict()
        print('----------obj_dicts')
        print(obj_dicts)
        with open(FileStorage.__file_path, "w") as write_to:
            json.dump(obj_dicts, write_to)

    def reload(self):
        """deserializes JSON in __file_path to __objects"""
        try:
            with open(FileStorage.__file_path, 'r') as read_from:
                data = json.load(read_from)
                print(type(data))
                for item in data.values():
                    class_name = item['__class__']
                    del item['__class__']
                    self.new(eval(class_name)(**item))
        except FileNotFoundError:
            print("file not found")
            return
        except json.JSONDecodeError:
            print("json decode error")
            return
