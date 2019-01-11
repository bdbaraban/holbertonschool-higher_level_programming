# 0-add_integer.txt
# Brennan D Baraban <375@holbertonschool.com>

===========================
How to Use 0-add_integer.py
===========================

This module defines an integer addition function ``add_integer(a, b=98)``.

Usage
=====

``add_integer(...)``` returns the addition of its two arguments. For numbers,
that value is equivalent to using the ``+`` operator.

::

    >>> add_integer = __import__('0-add_integer').add_integer
    >>> add_integer(2, 3)
    5

::

    >>> add_integer(2, -3)
    -1

The function also works with floating-point values.

::

    >>> add_integer(2.0, 3.0)
    5

Note that floats are casted to ints before addition is performed.

::

    >>> add_integer(2.9, 0.2)
    2

::

    >>> add_integer(-2.9, -0.2)
    -2

Floating and non-floating point values can be combined.

::

    >>> add_integer(2.3, -3)
    -1

The second argument is optional - by default, it is 98.

::

    >>> add_integer(2)
    100

Non-Numbers
===========

``add_integer()`` expects that both arguments are either integers or floats.
If either argument is a non-integer and non-float, a TypeError is raised:

::

    >>> add_integer("hello", 3)
    Traceback (most recent call last):
    TypeError: a must be an integer

::

    >>> add_integer(2, "hello")
    Traceback (most recent call last):
    TypeError: b must be an integer

::

    >>> add_integer(None)
    Traceback (most recent call last):
    TypeError: a must be an integer

::

    >>> add_integer(2.3, None)
    Traceback (most recent call last):
    TypeError: b must be an integer

If both arguments are non-integers and non-floats, a TypeError message is only
printed for the first argument.

::

    >>> add_integer("hello", "there")
    Traceback (most recent call last):
    TypeError: a must be an integer

The function will fail if infinity is provided.

::

    >>> add_integer(float('inf'))
    Traceback (most recent call last):
    OverflowError: cannot convert float infinity to integer
     

::

    >>> add_integer(2, float('inf'))
    Traceback (most recent call last):
    OverflowError: cannot convert float infinity to integer

And again with NaN numbers.

::

    >>> add_integer(float('nan'))
    Traceback (most recent call last):
    ValueError: cannot convert float NaN to integer

::

    >>> add_integer(2, float('nan'))
    Traceback (most recent call last):
    ValueError: cannot convert float NaN to integer
