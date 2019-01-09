# 3-say_my_name.txt
# Brennan D Baraban <375@holbertonschool.com>

===========================
How to Use 3-say_my_name.py
===========================

This modules defines a function ``say_my_name(first_name, last_name="")``.

Usage
=====

``say_my_name(...)`` prints "My name is <first_name> <last_name>".

::

    >>> say_my_name = __import__('3-say_my_name').say_my_name
    >>> say_my_name("Brennan", "Baraban")
    My name is Brennan Baraban

::

    >>> say_my_name("Cornelius Maxwell", "Jones II")
    My name is Cornelius Maxwell Jones II

The parameter ```last_name``` is optional. If no last name is provided,
an empty string is printed instead.

::

    >>> say_my_name("Brennan")
    My name is Brennan 

Invalid Names
=============

The parameters ``first_name`` and ``last_name``` must be strings. Otherwise,
a TypeError is raised.

::

    >>> say_my_name(6, "James")
    Traceback (most recent call last):
    TypeError: first_name must be a string

::

    >>> say_my_name("LeBron", ["Cavs", "Lakers", "Heat"])
    Traceback (most recent call last):
    TypeError: last_name must be a string

::

    >>> say_my_name({"LeBron": 6, "James": 23}, 7.7)
    Traceback (most recent call last):
    TypeError: first_name must be a string

::

    >>> say_my_name(None)
    Traceback (most recent call last):
    TypeError: first_name must be a string

At least one name must be provided.

::

    >>> say_my_name()
    Traceback (most recent call last):
    TypeError: say_my_name() missing 1 required positional argument: 'first_name'
