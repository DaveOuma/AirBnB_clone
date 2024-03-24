#!/usr/bin/python3
"""
Contains the Amenity model.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Model for Amenity objects.

    Attributes:
        name (str): The name of the amenity.
    """
    name = ""

