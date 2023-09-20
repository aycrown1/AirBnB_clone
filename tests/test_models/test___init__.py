#!/usr/bin/python3
import unittest
import sys
from io import StringIO
from console import HBNBCommand
from models import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class Test__init__(unittest.TestCase):
    'Class for testing __init__ in models'

    def tearDown(self):
        'called multiple times, once after each test'
        if os.path.exists("file.json"):
            try:
                os.remove("file.json")
            except:
                pass


if __name__ == "__main__":
    unittest.main()
