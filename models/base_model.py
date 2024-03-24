#!/usr/bin/python3
"""
Module implementing the BaseModel class.
"""

from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """
    Base class for other classes in the AirBnB clone project.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes the BaseModel instance.
        If kwargs is provided, sets instance attributes accordingly.
        Otherwise, generates a new UUID and sets created_at/updated_at.
        """
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                if key in ('created_at', 'updated_at'):
                    setattr(self, key, datetime.fromisoformat(value))

    def __str__(self):
        """
        Returns the string representation of the BaseModel object.
        """
        return "[{}] ({}) {}".format(type(self).__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates 'updated_at' with the current datetime and saves the object to storage.
        """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the BaseModel object.
        """
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = self.__class__.__name__
        for k, v in dict_1.items():
            if isinstance(v, datetime):
                dict_1[k] = v.isoformat()
        return dict_1

