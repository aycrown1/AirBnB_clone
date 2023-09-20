#!/usr/bin/python3
import unittest
from models.state import State

class TestState(unittest.TestCase):

    def test_attributes(self):
        # Test that State class has the expected attributes
        state = State()
        self.assertTrue(hasattr(state, 'name'))

    def test_attribute_types(self):
        # Test that the attribute types of State class are as expected
        state = State()
        self.assertIsInstance(state.name, str)

if __name__ == "__main__":
    unittest.main()
