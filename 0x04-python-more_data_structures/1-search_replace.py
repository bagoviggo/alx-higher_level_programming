#!/usr/bin/python3
"""function that replaces all occurrences of an element
by another in a new list."""


def search_replace(my_list, search, replace):
    if search in my_list:
        return [replace if x == search else x for x in my_list]
