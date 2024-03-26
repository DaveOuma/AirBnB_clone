#!/usr/bin/python3
"""
Contains the State model.
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    Model for State objects.

    Attributes:
        name (str): The name of the state.
    """

    name: str = ""

