#!/use/bin/python3
import uuid
from datetime import datetime
import models

"""
This module contains the parent class (called BaseModel)
          to take care of the initialization, serialization and
                   deserialization of the future instances.
All classes used for AirBnB (User, State, City, Place…) that
              inherit from BaseModel.
"""


class BaseModel:
    """
    This Class defines all common attributes/methods for other classes
    """
    def __init__(self, *args, **kwargs):
        """
        Initializes the id, created_at,
        and updated_at attributes when a new
        BaseModel instance is created.
        Args:
           id (str): initialized with a unique UUID as a string.
          created_at (datetime):
  initialized with the current datetime when an instance is created.
          updated_at (daytime): initialized with the current datetime
when an instance is created and it will be updated every time
the object is changed.
        """
        if kwargs:
            if kwargs["__class__"] == self.__class__.__name__:
                self.id, self.created_at, self.updated_at, *_ = kwargs.values()
                self.created_at = datetime.strptime(self.created_at,
                                                    "%Y-%m-%dT%H:%M:%S.%f")
                self.updated_at = datetime.strptime(self.updated_at,
                                                    "%Y-%m-%dT%H:%M:%S.%f")
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def save(self):
        """
        Updates the public instance attribute
             updated_at with the current datetime.
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all
             keys/values of __dict__ of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """
        print: [<class name>] (<self.id>) <self.__dict__>
        Returns:
                A string representation of the object,
        including class name, id, and its dictionary.
        """
        return f"[{self.__class__.__name__}] (self.id) [{self.__dict__}]"
