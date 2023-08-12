#!/usr/bin/python3
from models.base_model import BaseModel

"""my user class: with attribues of the user"""
class User(BaseModel):
    email = ""
    password = ""
    first_name = ""
    last_name = ""
