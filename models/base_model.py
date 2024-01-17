#!/usr/bin/python3
import uuid
from models import storage
from datetime import datetime

class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """constructor for basemodel class"""
        if kwargs:
            for key, value in kwargs.items():
                if key == "created_at" or key == "updated_at":
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key != "__class__":
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)


    def save(self):
        """Updates the public instance attribute
        updated_at with the current datetime"""

        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all
        keys/values of __dict__ of the instance"""

        new_dict = self.__dict__.copy()
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        new_dict["__class__"] = type(self).__name__
        return new_dict


    def __str__(self):
        """string representation of basemoel class"""

        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
