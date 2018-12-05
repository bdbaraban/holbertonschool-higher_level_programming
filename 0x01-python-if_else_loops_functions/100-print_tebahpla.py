#!/usr/bin/python3
# 100-print_tebahpla.py
# Brennan D Baraban <375@holbertonschool.com>

""""Print the alphabet in reverse order alternating upper- and lower-case."""
i = 0
for c in range(122, 96, -1):
    print("{}".format(chr(c - i)), end="")
    if i == 0:
        i = 32
    else:
        i = 0
