#!/usr/bin/python3
"""
Contains the City model.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    Model for City objects.

    Attributes:
        state_id (str): The ID of the state to which the city belongs.
        name (str): The name of the city.
    """
    state_id: str = ""
    name: str = ""

