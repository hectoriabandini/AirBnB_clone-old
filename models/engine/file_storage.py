#!/usr/bin/python3
""" storage module for base_model"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage():
    """
    storage main class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Return a dictionary of all objects.If a class name is provided."""
        if cls:
            objects_of_class = {}
            for key, value in self.__objects.items():
                if value.__class__.__name__ == cls:
                    objects_of_class[key] = value
                    return objects_of_class
                else:
                    return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            FileStorage.__objects[key] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict().copy()
        with open(FileStorage.__file_path, mode='w') as my_file:
            json.dump(new_dict, my_file)

    def reload(self):
        """
        public instance method that deserializes a JSON
        file to __objects.
        """
        try:
            with open(FileStorage.__file_path, mode='r') as my_file:
                new_dict = json.load(my_file)

            for key, value in new_dict.items():
                class_name = value.get('__class__')
                obj = eval(class_name + '(**value)')
                FileStorage.__objects[key] = obj

        except FileNotFoundError:
            pass

    def count(self, cls=None):
        """Count the number of instances of a class if cls is specified,
        otherwise count the total number of instances.
        """
        if cls is None:
            return len(self.__objects)
        else:
            count = 0
            for obj_id, obj in self.__objects.items():
                if obj.__class__.__name__ == cls:
                    count += 1
            return count
