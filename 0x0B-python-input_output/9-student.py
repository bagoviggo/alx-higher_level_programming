#!/usr/bin/python3
""" A class Student that defines a student by: """


class Student:
    """ A class Student that defines a student by: """

    def __init__(self, first_name, last_name, age):
        """ A class Student that defines a student by: """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ A class Student that defines a student by: """
        return self.__dict__
