#!/usr/bin/python3
# 1-number_of_lines.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines a text file line-counting function."""


def number_of_lines(filename=""):
    """Return the number of lines in a text file."""
    lines = 0
    with open(filename) as f:
        for line in f:
            lines += 1
    return lines
