#!/usr/bin/python3
"""Test suite for Review class in models.review"""
import unittest

from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class"""

    def setUp(self):
        """Set up a common environment for tests"""
        self.review = Review()
        self.attr_list = [
            "place_id",
            "user_id",
            "text"
        ]

    def test_review_is_a_subclass_of_basemodel(self):
        """Check if Review is a subclass of BaseModel"""
        self.assertTrue(issubclass(type(self.review), BaseModel))

    def test_attrs_are_class_attrs(self):
        """Check if attributes are class attributes"""
        for attr in self.attr_list:
            self.assertTrue(hasattr(self.review, attr))

    def test_class_attrs(self):
        """Check if attributes have correct types and default values"""
        for attr in self.attr_list:
            self.assertTrue(hasattr(self.review, attr))
            self.assertIs(type(getattr(self.review, attr)), str)
            self.assertFalse(getattr(self.review, attr))

if __name__ == "__main__":
    unittest.main()

