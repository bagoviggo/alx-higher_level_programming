#!/usr/bin/python3
"""Square class definition"""


class Square:
    """Module to find a square
    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size):
        """Initializes a square
        Args:
            size (int): size of a side of the square
        Returns: None
        """
        self.__size = size

        def area(self):
            """Calculatess the area of a square
            Returns: The area of the square
            """
            return self.__size ** 2

        @property
        def size(self):
            """getter for __size"""
            return self.__size

        @size.setter
        def size(self, value):
            """setter for __size"""
            if type(value) != int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

        def my_print(self):
            """Prints a square of #s"""
            if self.__size == 0:
                print()
            else:
                for i in range(self.__size):
                    print("#" * self.__size)
