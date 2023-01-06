#!/usr/bin/python3
"""This is a module that indents text"""


def text_indentation(text):
    """This function prints a text with two new lines after each of these characters: ., ? and :"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    for i in text:
        if i == '.' or i == '?' or i == ':':
            print(i)
            print()
        else:
            print(i, end="")
    print()
    