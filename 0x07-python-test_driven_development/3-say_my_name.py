#!/usr/bin/python3
""" This module prints a user's name """


def say_my_name(first_name, last_name=""):
    """ This function prints a user's name """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
