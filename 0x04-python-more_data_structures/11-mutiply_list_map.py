#!/usr/bin/python3
# 11-mutiply_list_map.py
# Brennan D Baraban <375@holbertonschool.com>


def mutiply_list_map(my_list=[], number=0):
    """Return a list with all values multiplied by a number."""
    return (list(map(lambda x: x*number, my_list)))
