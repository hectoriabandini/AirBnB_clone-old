#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from datetime import datetime

class TestBaseModel(unittest.TestCase):
    def setUp(self):
        self.my_model = BaseModel()
        self.my_model.name = "My First Model"
        self.my_model.my_number = 89

    def test_attributes(self):
        self.assertTrue(hasattr(self.my_model, "id"))
        self.assertTrue(hasattr(self.my_model, "created_at"))
        self.assertTrue(hasattr(self.my_model, "updated_at"))
        self.assertTrue(hasattr(self.my_model, "name"))
        self.assertTrue(hasattr(self.my_model, "my_number"))

    def test_str_method(self):
        expected = "[BaseModel] ({}) {}".format(self.my_model.id, self.my_model.__dict__)
        self.assertEqual(str(self.my_model), expected)

    def test_save_method(self):
        old_updated_at = self.my_model.updated_at
        self.my_model.save()
        new_updated_at = self.my_model.updated_at
        self.assertNotEqual(old_updated_at, new_updated_at)

    def test_to_dict_method(self):
        my_model_dict = self.my_model.to_dict()
        self.assertTrue(isinstance(my_model_dict, dict))
        self.assertEqual(my_model_dict['__class__'], 'BaseModel')
        self.assertEqual(my_model_dict['name'], 'My First Model')
        self.assertEqual(my_model_dict['my_number'], 89)
        self.assertEqual(type(my_model_dict['created_at']), str)
        self.assertEqual(type(my_model_dict['updated_at']), str)
        self.assertEqual(type(my_model_dict['id']), str)

    def test_to_dict_datetime_format(self):
        my_model_dict = self.my_model.to_dict()
        created_at = datetime.strptime(my_model_dict['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        updated_at = datetime.strptime(my_model_dict['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        self.assertEqual(created_at, self.my_model.created_at)
        self.assertEqual(updated_at, self.my_model.updated_at)

if __name__ == '__main__':
    unittest.main()
