#!/usr/bin/python3
# 3-print_alphabt.py
# Brennan D Baraban <375@holbertonschool.com>


"""Print the alphabet in lowercase except for the letters q and e."""
for letter in range(97, 123):
    if chr(letter) is not 'q' and chr(letter) is not 'e':
        print("{}".format(chr(letter)), end="")
