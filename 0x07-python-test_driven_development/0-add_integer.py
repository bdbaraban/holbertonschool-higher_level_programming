#!/usr/bin/python3
# 0-add_integer.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines an integer addition function."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    Float arguments are typecasted to ints before addition is performed.

    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float)) or
            a == float('inf') or a == -float('inf') or a != a):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float)) or
            b == float('inf') or b == -float('inf') or b != b):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
