#!/usr/bin/python3
""" This module contains a class that defines a rectangle """


class Rectangle:
    """ This is a class that represents a rectangle """
    def __init__(self, width=0, height=0):
        """ This is the constructor of the class """
        self.width = width
        self.height = height

    @property
    def width(self):
        """ This is the getter of the width attribute """
        return self.__width

    @width.setter
    def width(self, value):
        """ This is the setter of the width attribute """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ This is the getter of the height attribute """
        return self.__height

    @height.setter
    def height(self, value):
        """ This is the setter of the height attribute """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """ This method returns the area of the rectangle """
        return self.__width * self.__height

    def perimeter(self):
        """ This method returns the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """ This method returns the string representation of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join(["#" * self.__width] * self.__height)

    def __repr__(self):
        """ This method returns the string representation of the rectangle """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """ This method deletes an instance of the class """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
