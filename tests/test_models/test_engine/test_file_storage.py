#!/usr/bin/python3
import unittest
import os
from models import storage
from models.base_model import BaseModel

class TestFileStorage(unittest.TestCase):
    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage._FileStorage__objects.keys():
            del_list.append(key)
        for key in del_list:
            del storage._FileStorage__objects[key]

    def tearDown(self):
        # Clean up any temporary files created during testing
        if os.path.exists("file.json"):
            os.remove("file.json")

    def test_all(self):
        # Test the all() method to ensure it returns the correct dictionary
        # Initially, it should be empty
        self.assertEqual(self.storage.all(), {})

    def test_new(self):
        # Test the new() method to add a new object to __objects
        obj = BaseModel()
        self.storage.new(obj)
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.assertTrue(key in self.storage.all())

    def test_save(self):
        # Test the save() method to ensure it serializes objects to JSON
        obj = BaseModel()
        self.storage.new(obj)
        self.storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload_empty(self):
        """ Load from an empty file """
        with open('file.json', 'w') as f:
            pass
        with self.assertRaises(ValueError):
            storage.reload()

    def test_reload_from_nonexistent(self):
        """ Nothing happens if file does not exist """
        self.assertEqual(storage.reload(), None)


if __name__ == "__main__":
    unittest.main()
