#!/usr/bin/python3
"""Module with a function that returns a dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:"""


def class_to_json(obj):
    """A function that returns a dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:"""
    return obj.__dict__
