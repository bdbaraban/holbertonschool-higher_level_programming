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
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    if (not all(isinstance(row, list) for row in m_a) or
            not all(isinstance(row, list) for row in m_b)):
        raise TypeError("invalid data type for einsum")

    rows_a = len(m_a)
    cols_a = 0 if rows_a == 0 else len(m_a[0])
    rows_b = len(m_b)
    cols_b = 0 if rows_b == 0 else len(m_b[0])

    if m_a == [] or m_a == [[]] or m_a == [] or m_b == [[]]:
        raise ValueError("shapes ({},{}) and ({},{}) not aligned: {} (dim {}) "
                         "!= {} (dim {})".format(cols_b, rows_a,
                                                 cols_b, cols_b,
                                                 rows_a, rows_b,
                                                 cols_b, rows_a))

    if (not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in m_a for num in row]) or
        not all((isinstance(ele, int) or isinstance(ele, float))
                for ele in [num for row in m_b for num in row])):
        raise TypeError("invalid data type for einsum")

    if (not all(len(row) == len(m_a[0]) for row in m_a) or
            not all(len(row) == len(m_b[0]) for row in m_b)):
        raise TypeError("setting an array element with a sequence.")

    if cols_a != rows_b:
        raise ValueError("shapes ({},{}) and ({},{}) not aligned: {} (dim {}) "
                         "!= {} (dim {})".format(cols_b, rows_a,
                                                 cols_b, cols_b,
                                                 rows_a, rows_b,
                                                 cols_b, rows_a))

    a = np.array(m_a)
    b = np.array(m_b)
    return (a.dot(b))
