#!/usr/bin/python3
"""A class Student that defines a student by:(based on 9-student.py)"""

class Student:
    """A class Student that defines a student by:(based on 9-student.py)"""

    def __init__(self, first_name, last_name, age):
        """A class Student that defines a student by:(based on 9-student.py)"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A class Student that defines a student by:(based on 9-student.py)"""
        if type(attrs) is list and all(type(i) is str for i in attrs):
            return {i: getattr(self, i) for i in attrs if hasattr(self, i)}
        return self.__dict__

    def reload_from_json(self, json):
        """A class Student that defines a student by:(based on 9-student.py)"""
        for i, j in json.items():
            setattr(self, i, j)
