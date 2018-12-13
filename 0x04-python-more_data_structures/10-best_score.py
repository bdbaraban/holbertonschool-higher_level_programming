#!/usr/bin/python3
# 10-best_score.py
# Brennan D Baraban <375@holbertonschool.com>


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    big = list(a_dictionary.values())[0]
    ret = list(a_dictionary.keys())[0]
    for key in a_dictionary:
        if a_dictionary[key] > big:
            ret = key
    return (key)
