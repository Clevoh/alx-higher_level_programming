#!/usr/bin/python3
"""magic class definition"""
import math


class MagicClass:
    """magicclass that makes bytecode """

    def __init__(self, radius=0):
        """Initialize class"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        else:
            self.__radius = radius

    def area(self):
        """function that calculates area """
        return (self.__radius ** 2) * math.pi

    def circumference(self):
        """function that calculates circumference"""
        return (2 * math.pi) * self.__radius
