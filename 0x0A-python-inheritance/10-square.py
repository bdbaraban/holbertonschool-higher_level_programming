#!/usr/bin/python3
# 10-square.py
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
        super().integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """Return the area of the Square."""
        return super().area()
