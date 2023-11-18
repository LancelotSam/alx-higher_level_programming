#!/usr/bin/python3
"""Write the first cass Base"""
import json


class Base:
    """Base model.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize a new instnce of Base
        Args:
            id(int): number of instantiated Bases
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Return a JSON serialization of a list of
        dictionaries
        Args:
            list of dictionaries
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation
        of list_objs to file"""
        filename = clas.__name__ + ".json"
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                list_dicts = [o_to_dictionary() for o in list_objs]
                jsonfile.write(Base.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Return teh deseriealization f a JSON string"""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(clas, **dictionary):
        """Return a class instantied from a dictionary f attributes
        """
        if dictionary and dictionary != {}:
            if clas.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances"""
        filename = str(clas.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                list_dicts = Base.from_json_string(jsonfile.read())
                return [clas.create(**d) for d in list_dicts]
        except IOError:
            return []
