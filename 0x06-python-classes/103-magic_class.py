#!/usr/bin/python3
"""Define a class matching a bytecode provided by Holberton School."""
import math


class MagicClass:
    """Represent a magic class defining a circle."""

    def __init__(self, radius):
        """Initialize a magic class.

        Args:
            radius (int or float): The radius of the new MagicClass
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Return the circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
