#!/usr/bin/python3
# 0_add.py
# Brennan D Baraban <375@holbertonschool.com>

"""Print the result of the addition 1 + 2 = 3."""

if __name__ == "__main__":
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
