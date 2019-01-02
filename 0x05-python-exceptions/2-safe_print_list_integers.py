#!/usr/bin/python3
# 2-safe_print_list_integers.py
# Brennan D Baraban <375@holbertonschool.com>


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of a list that are integers."""
    ret = 0
    for i in range(0, x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except (ValueError, TypeError):
            continue
    print("")
    return (ret)
