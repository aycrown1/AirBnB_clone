#!/usr/bin/python3
import unittest
from datetime import datetime
from models.amenity import Amenity

class TestAmenity(unittest.TestCase):
    def test_attributes(self):
        # Test that Amenity class has the expected attributes
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, 'name'))
        self.assertTrue(hasattr(amenity, 'created_at'))
        self.assertTrue(hasattr(amenity, 'updated_at'))
        self.assertTrue(hasattr(amenity, 'id'))

    def test_attribute_types(self):
        # Test that the attribute types of Amenity class are as expected
        amenity = Amenity()
        self.assertIsInstance(amenity.name, str)
        self.assertIsInstance(amenity.created_at, datetime)
        self.assertIsInstance(amenity.updated_at, datetime)
        self.assertIsInstance(amenity.id, str)


if __name__ == "__main__":
    unittest.main()
