#!/usr/bin/python3
"""Test suite for the Place class of models.place"""
import unittest

from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases against the Place class"""

    def setUp(self):
        """Set up a common environment for tests"""
        self.place = Place()
        self.attr_list = ["name", "user_id", "city_id", "description",
                          "number_bathrooms", "max_guest", "number_rooms",
                          "price_by_night", "latitude", "longitude",
                          "amenity_ids"]

    def test_attrs_are_class_attrs(self):
        """Check if attributes are class attributes"""
        for attr in self.attr_list:
            self.assertTrue(hasattr(Place, attr))

    def test_class_attrs(self):
        """Check if attributes have correct types and default values"""
        for attr in self.attr_list:
            self.assertTrue(hasattr(self.place, attr))
            if attr in ["number_bathrooms", "max_guest", "number_rooms",
                        "price_by_night"]:
                self.assertIsInstance(getattr(self.place, attr), int)
                self.assertEqual(getattr(self.place, attr), 0)
            elif attr in ["latitude", "longitude"]:
                self.assertIsInstance(getattr(self.place, attr), float)
                self.assertEqual(getattr(self.place, attr), 0.0)
            elif attr == "amenity_ids":
                self.assertIsInstance(getattr(self.place, attr), list)
                self.assertEqual(getattr(self.place, attr), [])
            else:
                self.assertIsInstance(getattr(self.place, attr), str)
                self.assertEqual(getattr(self.place, attr), "")

    def test_place_obj_is_a_subclass_of_basemodel(self):
        """Check if Place object is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.place), BaseModel))


if __name__ == "__main__":
    unittest.main()

