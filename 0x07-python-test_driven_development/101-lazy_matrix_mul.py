#!/usr/bin/python3
# 101-lazy_matrix_mul.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines a matrix multiplication function using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a (list of lists of ints/floats): The first matrix.
        m_b (list of lists of ints/floats): The second matrix.
    Raises:
        TypeError: If either m_a or m_b is not a list of lists of ints/floats.
        TypeError: If either m_a or m_b is empty.
        TypeError: If either m_a or m_b has different-sized rows.
        ValueError: If m_a and m_b cannot be multiplied.
    Returns:
        A new matrix representing the multiplication of m_a by m_b.
    """

    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a is empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b is empty")

    if not isinstance(m_a, list):
        raise TypeError("m_a is not a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b is not a list")

    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a is not a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b is not a list of lists")

    if not all(len(row) == len(m_a[0]) for row in m_a):
        raise TypeError("m_a contains rows of different sizes")
    if not all(len(row) == len(m_b[0]) for row in m_b):
        raise TypeError("m_b contains rows of different sizes")

    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_a for num in row]):
        raise TypeError("m_a contains non-numbers")
    if not all((isinstance(ele, int) or isinstance(ele, float))
               for ele in [num for row in m_b for num in row]):
        raise TypeError("m_b contains non-numbers")

    a = np.array(m_a)
    b = np.array(m_b)

    try:
        return (a.dot(b))
    except ValueError:
        raise ValueError("cannot multiply - m_a and m_b are unaligned")
