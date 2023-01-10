#!/usr/bin/python3
"""a function that creates an Object from a “JSON file”:"""


def load_from_json_file(filename):
    """a function that creates an Object from a “JSON file”:"""
    import json
    with open(filename, 'r', encoding='utf-8') as file:
        return json.loads(file.read())
