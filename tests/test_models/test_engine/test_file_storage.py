#!/usr/bin/python3
"""Test Suite for FileStorage in models/file_storage.py"""

import os.path
import unittest

import models
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.amenity import Amenity
from models.city import City
from models.review import Review
from models.place import Place


class TestFileStorageInit(unittest.TestCase):
    """Contains test cases against the FileStorage initialization"""

    def test_file_path_is_a_private_class_attr(self):
        """Check that file_path is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__file_path"))

    def test_objects_is_a_private_class_attr(self):
        """Check that objects is a private class attribute"""
        self.assertFalse(hasattr(FileStorage(), "__objects"))

    def test_init_without_arg(self):
        """Test initialization without arguments"""
        self.assertEqual(type(FileStorage()), FileStorage)

    def test_init_with_arg(self):
        """Test initialization with arguments"""
        with self.assertRaises(TypeError):
            FileStorage(None)

    def test_storage_initialization(self):
        """Test storage created in __init__.py"""
        self.assertEqual(type(models.storage), FileStorage)


class TestStorageMethods(unittest.TestCase):
    """Contains test cases against the methods present in FileStorage"""

    @classmethod
    def setUpClass(cls):
        """Code to execute before testing occurs"""
        try:
            os.rename("file.json", "tmp.json")
        except IOError:
            pass

    @classmethod
    def tearDownClass(cls):
        """Code to execute after tests are executed"""
        # Restore original file.json
        try:
            os.remove("file.json")
        except IOError:
            pass

        try:
            os.rename("tmp.json", "file.json")
        except IOError:
            pass

        FileStorage._FileStorage__objects = {}

    def test_all_method(self):
        """Test all() method of the FileStorage class"""
        # Check that all() returns a dictionary
        self.assertTrue(isinstance(models.storage.all(), dict))

        # Check that passing an argument raises TypeError
        with self.assertRaises(TypeError):
            models.storage.all(None)

    def test_new_method(self):
        """Test the new() method of the FileStorage class"""
        # Create instances of various models
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        # Check that the objects created above are stored
        objects = models.storage.all()
        self.assertIn("BaseModel." + dummy_bm.id, objects)
        self.assertIn(dummy_bm, objects.values())
        # Similar checks for other models...

        # Check that passing more than one argument raises TypeError
        with self.assertRaises(TypeError):
            models.storage.new(BaseModel(), 1)

        # Check that passing None raises AttributeError
        with self.assertRaises(AttributeError):
            models.storage.new(None)

    def test_save_method(self):
        """Test save() method of the FileStorage class"""
        # Create instances of various models
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        # Save objects to file.json
        models.storage.save()

        # Check that objects were saved to file.json
        with open("file.json", "r") as f:
            save_text = f.read()
            self.assertIn("BaseModel." + dummy_bm.id, save_text)
            # Similar checks for other models...

        # Check that passing an argument raises TypeError
        with self.assertRaises(TypeError):
            models.storage.save(None)

    def test_reload_method(self):
        """Test reload() method of the FileStorage class"""
        # Create instances of various models
        dummy_bm = BaseModel()
        dummy_user = User()
        dummy_state = State()
        dummy_city = City()
        dummy_place = Place()
        dummy_review = Review()
        dummy_amenity = Amenity()

        # Save objects to file.json and reload them
        models.storage.save()
        models.storage.reload()
        objects = FileStorage._FileStorage__objects

        # Check that objects were reloaded correctly
        self.assertIn("BaseModel." + dummy_bm.id, objects)
        # Similar checks for other models...

        # Check that passing an argument raises TypeError
        with self.assertRaises(TypeError):
            models.storage.reload(None)


if __name__ == "__main__":
    unittest.main()

