#!/usr/bin/python3


class Square:
    """Represents a square  """
    size = 0
    def __init__(self, size):
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
