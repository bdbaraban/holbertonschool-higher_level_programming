#!/usr/bin/python3
# 0-positive_or_negative.py
# Brennan D Baraban <375@holbertonschool.com>

"""Generate a random number and print whether it is positive or negative."""
import random
number = random.randint(-10, 10)
if number > 0:
    print("{} is positive".format(number))
elif number == 0:
    print("{} is zero".format(number))
else:
    print("{} is negative".format(number))
