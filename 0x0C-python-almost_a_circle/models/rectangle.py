#!/usr/bin/python3
""" Base class: rectangle """
from models.base import Base


class Base:
    """ Rectangle class """

    def __init__(self, width, height, x=0, y=0, id=None):
        """ the equivalent of initializing a function """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Set the width """
        return self.__width

    @width.setter
    def width(self, value):
        """ Set the width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
                raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ Remember: Decorators allow for attributes to be modified """
        return self.__height

    @height.setter
    def height(self, value):
        """ Set the height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def x(self):
        """ Set the value of x """
        return self.__x

    @x.setter
    def x(self, value):
        """ Set the x value """
        self.__x = value

    @property
    def y(self):
        """ Set the value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ Set the y value """
        self.__y = value