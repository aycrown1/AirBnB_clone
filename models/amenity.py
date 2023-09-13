#!/usr/bin/python3
"""Defines the Amenity class that inherits from the BaseModel"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Represent an amenity.

    Attributes:
        name (str): The name of the amenity.
    """

    name = ""
