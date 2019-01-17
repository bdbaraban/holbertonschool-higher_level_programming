#!/usr/bin/python3
# 11-square.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines a Rectangle subclass Square."""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle, BaseGeometry):
    """Represent a square."""

    def __init__(self, size):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
        """
        super().__init__(size, size)
        self.__size = size

    def area(self):
        """Return the area of the Square."""
        return self.__size * self.__size

    def __str__(self):
        """Return the print() and str() representation of a Square."""
        string = "[Square] " + str(self.__size)
        string += "/" + str(self.__size)
        return string
