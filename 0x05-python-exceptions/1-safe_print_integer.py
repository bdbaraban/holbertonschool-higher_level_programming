#!/usr/bin/python3
# 1-safe_print_integer.py
# Brennan D Baraban <375@holbertonschool.com>


def safe_print_integer(value):
    """Print an integer with "{:d}".format().

    Args:
        value (int): The integer to print.

    Returns:
        If a ValueError occurs - False.
        Otherwise - True.
    """
    try:
        print("{:d}".format(value))
        return (True)
    except ValueError:
        return (False)
