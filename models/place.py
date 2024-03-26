#!/usr/bin/python3
"""
Contains the Place model.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Model for Place objects.

    Attributes:
        city_id (str): The ID of the city to which the place belongs.
        user_id (str): The ID of the user who owns the place.
        name (str): The name of the place.
        description (str): The description of the place.
        number_rooms (int): The number of rooms of the place. (default: 0)
        number_bathrooms (int): The number of bathrooms of the place. (default: 0)
        max_guest (int): The maximum number of guests of the place. (default: 0)
        price_by_night (int): The price per night of the place. (default: 0)
        latitude (float): The latitude of the place. (default: 0.0)
        longitude (float): The longitude of the place. (default: 0.0)
        amenity_ids (list): A list of Amenity IDs.
    """

    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str = ""
    number_rooms: int = 0
    number_bathrooms: int = 0
    max_guest: int = 0
    price_by_night: int = 0
    latitude: float = 0.0
    longitude: float = 0.0
    amenity_ids: list = []

