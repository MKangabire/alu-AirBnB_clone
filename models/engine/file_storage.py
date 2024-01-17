#!/usr/bin/python3

import json

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    @property
    def file_path(self):
        return self.__file_path

    @property
    def _FileStorage__objects(self):
        return FileStorage.__objects

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def delete(self, key):
        ''' Deletes an object from __objects if it is inside
        '''
        if key in FileStorage.__objects.keys():
            del FileStorage.__objects[key]
            self.save()

    def save(self):
        """ Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, mode='w', encoding="utf-8") as f:
            copied_dict = {}
            for key, value in FileStorage.__objects.items():
                copied_dict[key] = value.to_dict()
            json.dump(copied_dict, f)
    def reload(self):
        """Deserialize the JSON file to __objects"""

        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        try:
            with open(self.file_path, mode='r', encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                     FileStorage.__objects[key] = eval(
                        value["__class__"])(**value)
        except NameError:
            pass
        except IOError:
            pass
