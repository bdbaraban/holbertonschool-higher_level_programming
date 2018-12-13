#!/usr/bin/python3
# 9-multiple_by_2.py
# Brennan D Baraban <375@holbertonschool.com>


def multiply_by_2(a_dictionary):
    """Return a new dictionary with all values multipled by 2."""
    return ({k: a_dictionary[k] * 2 for k in a_dictionary})
