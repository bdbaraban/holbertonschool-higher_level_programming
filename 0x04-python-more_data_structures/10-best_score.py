#!/usr/bin/python3
# 10-best_score.py
# Brennan D Baraban <375@holbertonschool.com>


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict):
        return None

    x = 0
    for key in a_dictionary:
        if a_dictionary[key] > x:
            ret = key
    return (key)
