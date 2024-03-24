#!/usr/bin/python3
"""Test suite for the City class of the models.city module"""
import unittest

from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class"""

    def setUp(self):
        """Set up a common environment for tests"""
        self.city = City()
        self.attr_list = ["state_id", "name"]

    def test_city_is_a_subclass_of_basemodel(self):
        """Check if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.city), BaseModel))

    def test_attrs_are_class_attrs(self):
        """Check if attributes are class attributes"""
        for attr in self.attr_list:
            self.assertIsInstance(getattr(self.city, attr), str)
            self.assertEqual(getattr(self.city, attr), "")

    def test_attr_types(self):
        """Check if attributes have correct types"""
        for attr in self.attr_list:
            self.assertIsInstance(getattr(self.city, attr), str)

    def test_attr_initialization(self):
        """Check if attributes are initialized correctly"""
        for attr in self.attr_list:
            self.assertEqual(getattr(self.city, attr), "")

    def test_setting_attr_to_non_str(self):
        """Check if setting attribute to non-str type raises TypeError"""
        for attr in self.attr_list:
            with self.assertRaises(TypeError):
                setattr(self.city, attr, 123)

    def test_setting_attr_to_str(self):
        """Check if setting attribute to str type works"""
        for attr in self.attr_list:
            setattr(self.city, attr, "test")
            self.assertEqual(getattr(self.city, attr), "test")


if __name__ == "__main__":
    unittest.main()

