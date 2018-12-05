#!/usr/bin/python3
# 0_add.py
# Brennan D Baraban <375@holbertonschool.com>

if __name__ == "__main__":
    """Print the sum of 1 and 2."""
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
