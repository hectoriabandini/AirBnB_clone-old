#!/usr/bin/python3
"""
this module brings together all other classes like
{City}, {State}, {Amenity} to define a particular place
or location in this app
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class:
        handles collection of data from city,state and amenity
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
