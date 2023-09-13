#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Return the dictionary of objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Add a new object to __objects."""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serialize __objects to the JSON file."""
        serialized_objs = {}
        for key, obj in FileStorage.__objects.items():
            serialized_objs[key] = obj.to_dict()

        with open(FileStorage.__file_path, 'w') as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """Deserializes the JSON file to __objects
(only if the JSON file (__file_path) exists;
        otherwise, do nothing. If the file doesn’t exist,
no exception should be raised)
        """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, obj_id = key.split('.')
                    obj = globals()[class_name](**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
