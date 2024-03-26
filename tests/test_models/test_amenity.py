#!/usr/bin/python3
"""Test suite for Amenity class of the models.amenity module"""
import unittest

from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class"""

    def setUp(self):
        """Set up a test instance of Amenity"""
        self.amenity = Amenity()

    def test_amenity_is_a_subclass_of_basemodel(self):
        """Test if Amenity is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.amenity), BaseModel))

    def test_attr_is_a_class_attr(self):
        """Test if 'name' attribute is a class attribute of Amenity"""
        self.assertTrue(hasattr(self.amenity, "name"))

    def test_class_attr(self):
        """Test if 'name' attribute of Amenity is of type string and initially empty"""
        self.assertIs(type(self.amenity.name), str)
        self.assertFalse(bool(self.amenity.name))


if __name__ == "__main__":
    unittest.main()

