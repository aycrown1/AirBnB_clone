#!/usr/bin/python3
import unittest
from models.user import User

class TestUser(unittest.TestCase):

    def test_attributes(self):
        # Test that User class has the expected attributes
        user = User()
        self.assertTrue(hasattr(user, 'email'))
        self.assertTrue(hasattr(user, 'password'))
        self.assertTrue(hasattr(user, 'first_name'))
        self.assertTrue(hasattr(user, 'last_name'))

    def test_attribute_types(self):
        # Test that the attribute types of User class are as expected
        user = User()
        self.assertIsInstance(user.email, str)
        self.assertIsInstance(user.password, str)
        self.assertIsInstance(user.first_name, str)
        self.assertIsInstance(user.last_name, str)

if __name__ == "__main__":
    unittest.main()
