# 2-matrix_divided.txt
# Brennan D Baraban <375@holbertonschool.com>

==============================
How to Use 2-matrix_divided.py
==============================

This module defines a matrix division function ``matrix_divided(matrix, div)``.

Usage
=====

``matrix_divided(...)`` returns a new matrix that is a copy of the parameter
``matrix`` with all elements divided by ``div``.

::

    >>> matrix_divided = __import__('2-matrix_divided').matrix_divided
    >>> matrix = [
    ...     [3, 6, 9],
    ...     [12, 15, 18]
    ... ]
    >>> print(matrix_divided(matrix, 3))
    [[1.0, 2.0, 3.0], [4.0, 5.0, 6.0]]

Note that quotients are rounded to a maximum of two decimal places.

::

    >>> matrix = [
    ...     [1, 2, 3],
    ...     [4, 5, 6]
    ... ]
    >>> print(matrix_divided(matrix, 3))
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]

The original matrix is left unchanged.

::

    >>> print(matrix)
    [[1, 2, 3], [4, 5, 6]]

The function can also handle floating-point numbers.

::

    >>> matrix = [
    ...     [1.1, -2.2, 3.3],
    ...     [4.4, 5.5, -6.6]
    ... ]
    >>> print(matrix_divided(matrix, 3))
    [[0.37, -0.73, 1.1], [1.47, 1.83, -2.2]]

Integers and floats can be combined.

::

    >>> matrix = [
    ...     [1, -2.2, 3, 4.4, 5],
    ...     [-6.6, 7.00, 8, 9.999, 10]
    ... ]
    >>> print(matrix_divided(matrix, 3))
    [[0.33, -0.73, 1.0, 1.47, 1.67], [-2.2, 2.33, 2.67, 3.33, 3.33]]

Invalid Matrices
==============

The parameter ``matrix`` must be a list of lists consisting of either ints or
floats. If ``matrix`` is not a list, a TypeError is raised.

::

    >>> matrix = "not a list"
    >>> print(matrix_divided(matrix, 3))
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

::

    >>> matrix = None
    >>> print(matrix_divided(matrix, 3))
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

Note that an empty list will raise the TypeError.

::

    >>> matrix = []
    >>> print(matrix_divided(matrix, 3))
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

But an empty list of lists will succeed.

::

    >>> matrix = [[]]
    >>> print(matrix_divided(matrix, 3))
    [[]]

An identical TypeError is raised if ``matrix`` is not specifically a list of
lists.

::

    >>> matrix = [1, 2, 3]
    >>> print(matrix_divided(matrix, 3))
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats

The same TypeError is raised yet again if any elements in ``matrix`` are
neither ints nor floats.

::

    >>> matrix = [
    ...     [1, 2, 3],
    ...     [4, "not a number", 6]
    ... ]
    >>> print(matrix_divided(matrix, 3))
    Traceback (most recent call last):
    TypeError: matrix must be a matrix (list of lists) of integers/floats


Finally, all the rows in ``matrix`` must be the same size. If any rows are
of different sizes, a new TypeError is raised.

::

    >>> matrix = [
    ...     [1, 2, 3, 4],
    ...     [5, 6, 7]
    ... ]
    >>> print(matrix_divided(matrix, 3))
    Traceback (most recent call last):
    TypeError: Each row of the matrix must have the same size

Invalid Divisors
================

The parameter ``div`` must be either an int or float. Otherwise, a TypeError
is raised.

::

    >>> matrix = [
    ...     [1, 2, 3],
    ...     [4, 5, 6]
    ... ]
    >>> print(matrix_divided(matrix, "not a number"))
    Traceback (most recent call last):
    TypeError: div must be a number

::

    >>> print(matrix_divided(matrix, None))
    Traceback (most recent call last):
    TypeError: div must be a number

``div`` must also be non-zero. Otherwise, a ZeroDivisionError is raised.

::

    >>> print(matrix_divided(matrix, 0))
    Traceback (most recent call last):
    ZeroDivisionError: division by zero
