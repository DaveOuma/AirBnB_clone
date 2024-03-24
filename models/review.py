#!/usr/bin/python3
"""
Contains the Review model.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Model for Review objects.

    Attributes:
        place_id (str): The ID of the place being reviewed.
        user_id (str): The ID of the user who wrote the review.
        text (str): The text content of the review.
    """

    place_id: str = ""
    user_id: str = ""
    text: str = ""

