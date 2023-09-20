#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
import models

class TestBaseModel(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def test_attributes(self):
        # Test that BaseModel class has the expected attributes
        base_model = BaseModel()
        self.assertTrue(hasattr(base_model, 'id'))
        self.assertTrue(hasattr(base_model, 'created_at'))
        self.assertTrue(hasattr(base_model, 'updated_at'))

    def test_attribute_types(self):
        # Test that the attribute types of BaseModel class are as expected
        base_model = BaseModel()
        self.assertIsInstance(base_model.id, str)
        self.assertIsInstance(base_model.created_at, datetime)
        self.assertIsInstance(base_model.updated_at, datetime)

    def test_save(self):
        # Test the save() method of BaseModel class
        base_model = BaseModel()
        original_updated_at = base_model.updated_at
        base_model.save()

        self.assertNotEqual(base_model.updated_at, original_updated_at)

    def test_todict(self):
        """ """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

if __name__ == "__main__":
    unittest.main()

