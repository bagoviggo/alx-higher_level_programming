#!/usr/bin/python3
"""This is a module that reads a text file (UTF8) and prints it to stdout:"""


def read_file(filename=""):

    with open(filename, encoding="utf-8") as file:
        for line in file:
            print(line.rstrip())
