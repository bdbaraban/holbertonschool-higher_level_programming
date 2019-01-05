#!/usr/bin/python3
# 3-safe_print_division.py
# Brennan D Baraban <375@holbertonschool.com>


def safe_print_division(a, b):
    """Returns the division of a by b."""
    try:
        div = a / b
    except (TypeError, ZeroDivisionError):
        div = None
    finally:
        print("Inside result: {}".format(div))
    return (div)
