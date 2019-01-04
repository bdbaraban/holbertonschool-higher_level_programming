#!/usr/bin/python3
# 5-square.py
# Brennan D Baraban<375@holbertonschool.com>
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square.

        Args:
            size (int): The size of the new square.
            position (int, int): The position of the new square.
        """
        if not isinstance(size, int):
            print("size must be an integer", end="")
            raise TypeError
        elif size < 0:
            print("size must be >= 0", end="")
            raise ValueError
        if (not isinstance(position[0], int) or
                not isinstance(position[1], int) or
                position[0] < 0 or position[1] < 0):
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        self.__size = size
        self.__position = position

    @property
    def size(self):
        """Get/set the current size of the square.

        Args:
            value (int): The new size of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            print("size must be an integer", end="")
            raise TypeError
        elif value < 0:
            print("size must be >= 0", end="")
            raise ValueError
        self.__size = value

    @property
    def position(self):
        """Get/set the current position of the square.

        Args:
            value (int, int): The new position of the square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            print("position must be a tuple of 2 positive integers")
            raise TypeError
        self.__position = value

    def area(self):
        """Return the current area of the square."""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        for i in range(0, self.__size):
            [print(" ", end="") for i in range(0, self.__position[0])]
            [print("#", end="") for j in range(0, self.__size)]
            print("")
        if self.__size == 0:
            print("")
