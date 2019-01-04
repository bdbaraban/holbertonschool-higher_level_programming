#!/usr/bin/python3
# 2-square.py
# Brennan D Baraban<375@holbertonschool.com>
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square.
        """
        if not isinstance(size, int):
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = size
