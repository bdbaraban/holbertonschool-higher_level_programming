#!/usr/bin/python3
# 101-locked_class.py
# Brennan D Baraban <375@holbertonschool.com>
"""Defines a locked class."""


class LockedClass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
