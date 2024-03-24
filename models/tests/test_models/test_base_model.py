#!/usr/bin/python3
"""
A module that contains the test suite for the BaseModel class
"""
import unittest
from time import sleep
import os
from datetime import datetime
from uuid import uuid4

import models
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    The test suite for models.base_model.BaseModel
    """

    def setUp(self):
        """Set up a common environment for tests"""
        self.b = BaseModel()

    def tearDown(self):
        """Clean up after each test"""
        del self.b

    def test_id_assigned_on_initialization(self):
        """Checks that instance has an id assigned on initialization"""
        self.assertTrue(hasattr(self.b, "id"))

    def test_str_representation(self):
        """Checks if the string representation is appropriate"""
        expected_str = "[BaseModel] ({}) {}".format(self.b.id, self.b.__dict__)
        self.assertEqual(str(self.b), expected_str)

    def test_unique_ids_generated(self):
        """Checks if id is generated randomly and uniquely"""
        other_b = BaseModel()
        self.assertNotEqual(self.b.id, other_b.id)

    def test_type_of_id_is_str(self):
        """Checks that id generated is a str object"""
        self.assertIsInstance(self.b.id, str)

    def test_created_at_is_datetime(self):
        """Checks that the attribute 'created_at' is a datetime object"""
        self.assertIsInstance(self.b.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """Checks that the attribute 'updated_at' is a datetime object"""
        self.assertIsInstance(self.b.updated_at, datetime)

    def test_created_at_less_than_updated_at_initially(self):
        """Checks that created_at < updated_at at initialization"""
        self.assertLess(self.b.created_at, self.b.updated_at)

    def test_save_updates_updated_at(self):
        """Checks that save() method updates the updated_at attribute"""
        prev_updated_at = self.b.updated_at
        self.b.save()
        self.assertGreater(self.b.updated_at, prev_updated_at)

    def test_to_dict_returns_dict(self):
        """Checks if BaseModel.to_dict() returns a dict object"""
        self.assertIsInstance(self.b.to_dict(), dict)

    def test_to_dict_contains_all_keys(self):
        """Checks whether to_dict() returns the expected keys"""
        expected_keys = ["id", "created_at", "updated_at", "__class__"]
        self.assertListEqual(list(self.b.to_dict().keys()), expected_keys)

    def test_to_dict_contains_correct_values(self):
        """Checks if values in to_dict() match the BaseModel attributes"""
        for key, value in self.b.to_dict().items():
            if key == "__class__":
                self.assertEqual(value, "BaseModel")
            else:
                self.assertEqual(value, getattr(self.b, key))

    def test_to_dict_with_args(self):
        """Checks that TypeError is raised when argument is passed to to_dict()"""
        with self.assertRaises(TypeError):
            self.b.to_dict(None)

    def test_save_method_updates_file(self):
        """Tests if file is updated when the 'save' is called"""
        self.b.save()
        with open("file.json", encoding="utf-8") as f:
            self.assertIn("BaseModel.{}".format(self.b.id), f.read())

    def test_storage_new_not_called_with_dict(self):
        """Checks that storage.new() is not called when BaseModel is created from a dict"""
        self.assertIsInstance(self.b, BaseModel)
        self.assertNotIn(self.b, models.storage.all().values())

    def test_save_updates_updated_at(self):
        """Checks that save() method updates 'updated_at' attribute"""
        prev_updated_at = self.b.updated_at
        sleep(0.02)
        self.b.save()
        self.assertGreater(self.b.updated_at, prev_updated_at)

    def test_save_updates_file_twice(self):
        """Tests that the save method updates 'updated_at' two times"""
        self.b.save()
        prev_updated_at = self.b.updated_at
        sleep(0.02)
        self.b.save()
        self.assertGreater(self.b.updated_at, prev_updated_at)

    def test_to_dict_not_dunder_dict(self):
        """Checks that to_dict() is a dict object not equal to __dict__"""
        self.assertNotEqual(self.b.to_dict(), self.b.__dict__)


if __name__ == "__main__":
    unittest.main()

