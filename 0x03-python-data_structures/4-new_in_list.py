#!/usr/bin/python3
# 4-new_in_list.py
# Brennan D Baraban <375@holbertonschool.com>


def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    if idx >= 0 and idx < len(my_list):
        copy = [x for x in my_list]
        copy[idx] = element
    return (copy)
