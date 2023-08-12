#!/usr/bin/python3
"""City address within a state also carrying state id"""
from models.base_model import BaseModel
class City(BaseModel):
    state_id = ""
    name = ""
