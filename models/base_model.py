#!/usr/bin/python3

"""
this model contians class BaseModel
"""
from uuid import uuid4
from datetime import datetime
import models


class BaseModel:
    """
    class BaseModel
    """
    def __init__(self, *args, **kwargs):
        """
        init class
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

        if len(kwargs) > 1:
            date_format = '%Y-%m-%dT%H:%M:%S.%f'
            for key, value in kwargs.items():
                if key != '__class__':
                    self.__dict__[key] =  value

                if key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.strptime(value, date_format)
        else:
            models.storage.new(self)


    def __str__(self):
        """string representation of class"""
        return "[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """save instance"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        this method returns dict of instance
        """
        #new_dict = self.__dict__.copy()
        self.__dict__['__class__'] = self.__class__.__name__
        self.__dict__['created_at'] = self.created_at.isoformat()
        self.__dict__['updated_at'] = self.updated_at.isoformat()
        return self.__dict__
