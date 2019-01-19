# 7-base_geometry.txt
# Brennan D Baraban <375@holbertonschool.com>

=============================
How to Use 7-base_geometry.py
=============================

This modules defines a base geometry class BaseGeometry.

Instantiation
=============

``BaseGeometry`` includes no attributes, and accordingly is initialized 
with no arguments.

::

    >>> BaseGeometry = __import__('7-base_geometry').BaseGeometry
    >>> bg = BaseGeometry()
    >>> type(bg)
    <class '7-base_geometry.BaseGeometry'>

::

    >>> print(bg) # doctest: +ELLIPSIS
    <7-base_geometry.BaseGeometry object at ...>

In fact, any arguments supplied to an instantiation of ``BaseGeometry`` results
in a TypeError.

::

    >>> bg = BaseGeometry(None)
    Traceback (most recent call last):
    TypeError: object() takes no parameters

Methods
=======

``BaseGeometry`` features two methods - ``area(self)`` and 
``integer_validator(self, name, value)``. ``area(...)`` is not yet
implemented.

::

    >>> bg = BaseGeometry()
    >>> print(bg.area) # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    <bound method BaseGeometry.area of <7-base_geometry.BaseGeometry 
     object at...>>

::

    >>> bg.area()
    Traceback (most recent call last):
    Exception: area() is not implemented

The second method, ``integer_validator(...)``, validates the integer value
of a paramter. The first parameter, ``name``, is the name of the argument to
check. The second argument, ``value``, is the argument to check.

::

    >>> print(bg.integer_validator) # doctest: +ELLIPSIS, +NORMALIZE_WHITESPACE
    <bound method BaseGeometry.integer_validator of <7-base_geometry.BaseGeometry 
    object at...>>

If ``value`` is a valid integer, the function does nothing.

::


   >>> bg.integer_validator("valid number", 1)

But, if ``value`` is not an integer, a ``TypeError`` is raised.

::

    >>> bg.integer_validator("invalid number", "number")
    Traceback (most recent call last):
    TypeError: invalid number must be an integer

::

    >>> bg.integer_validator("another invalid", True)
    Traceback (most recent call last):
    TypeError: another invalid must be an integer

::

    >>> bg.integer_validator("invalid tuple", (1,))
    Traceback (most recent call last):
    TypeError: invalid tuple must be an integer

::

    >>> bg.integer_validator("and another", [3])
    Traceback (most recent call last):
    TypeError: and another must be an integer

::

    >>> bg.integer_validator("more invalid testing", {3, 4})
    Traceback (most recent call last):
    TypeError: more invalid testing must be an integer

::

    >>> bg.integer_validator("absolutely every possible invalid", None)
    Traceback (most recent call last):
    TypeError: absolutely every possible invalid must be an integer

And if ``value`` is an integer, but less than or equal to zero, a ValueError
is raised.

::

    >>> bg.integer_validator("invalid int", -1)
    Traceback (most recent call last):
    ValueError: invalid int must be greater than 0

::

    >>> bg.integer_validator("invalid int", 0)
    Traceback (most recent call last):
    ValueError: invalid int must be greater than 0

Both ``name`` and ``value`` must be provided. Otherwise, a TypeError is raised.

::

    >>> bg.integer_validator() # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    TypeError: integer_validator() missing 2 required positional arguments: 
    'name' and 'value'

::

    >>> bg.integer_validator(None) # doctest: +NORMALIZE_WHITESPACE
    Traceback (most recent call last):
    TypeError: integer_validator() missing 1 required positional argument: 
    'value'

The method assumes the paramter ``name`` will be a string, but ``name`` of any
type will be printed.

::

    >>> bg.integer_validator({"a": 1}, (1, 2))
    Traceback (most recent call last):
    TypeError: {'a': 1} must be an integer
