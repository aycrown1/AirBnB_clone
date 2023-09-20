#!/usr/bin/python3
import unittest
from models.review import Review

class TestReview(unittest.TestCase):

    def test_attributes(self):
        # Test that Review class has the expected attributes
        review = Review()
        self.assertTrue(hasattr(review, 'place_id'))
        self.assertTrue(hasattr(review, 'user_id'))
        self.assertTrue(hasattr(review, 'text'))

    def test_attribute_types(self):
        # Test that the attribute types of Review class are as expected
        review = Review()
        self.assertIsInstance(review.place_id, str)
        self.assertIsInstance(review.user_id, str)
        self.assertIsInstance(review.text, str)

if __name__ == "__main__":
    unittest.main()
