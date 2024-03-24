#!/usr/bin/python3
"""
Module containing the FileStorage class model.

This module provides a FileStorage class that serializes instances to a JSON file
and deserializes JSON file to instances. It serves as a storage engine for storing
and retrieving objects related to the AirBnB clone project.

Classes:
    FileStorage: A class that manages serialization and deserialization of instances.

"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review

class FileStorage:
    """
    A class that serializes instances to a JSON file and deserializes JSON file to instances.

    Attributes:
        __file_path (str): The path to the JSON file.
        __objects (dict): A dictionary containing all serialized instances.

    Methods:
        all(): Returns the dictionary of serialized objects.
        new(obj): Adds a new object to the dictionary of serialized objects.
        save(): Serializes the dictionary of objects to the JSON file.
        reload(): Deserializes the JSON file to populate the dictionary of objects.

    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of serialized objects.

        Returns:
            dict: A dictionary containing all serialized objects.

        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of serialized objects.

        Args:
            obj: The object to be serialized.

        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """
        Serializes the dictionary of objects to the JSON file.

        """
        with open(self.__file_path, mode="w") as f:
            dict_storage = {k: v.to_dict() for k, v in self.__objects.items()}
            json.dump(dict_storage, f)

    def reload(self):
        """
        Deserializes the JSON file to populate the dictionary of objects.
        Only reloads if the JSON file exists.

        """
        try:
            with open(self.__file_path, encoding="utf-8") as f:
                for obj in json.load(f).values():
                    self.new(eval(obj["__class__"])(**obj))
        except FileNotFoundError:
            pass
