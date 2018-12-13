#!/usr/bin/python3
# 10-best_score.py
# Brennan D Baraban <375@holbertonschool.com>


def best_score(a_dictionary):
    """Returns a key with the biggest integer value."""
    if not isinstance(a_dictionary, dict) or len(a_dictionary) == 0:
        return None

    ret = list(a_dictionary.keys())[0]
    big = a_dictionary[ret]
    for k, v in a_dictionary.items():
        if v > big:
            big = v
            ret = k
    return (ret)
