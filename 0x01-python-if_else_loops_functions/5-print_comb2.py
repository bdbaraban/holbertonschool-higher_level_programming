#!/usr/bin/python3
# 5-print_comb2.py
# Brennan D Baraban <375@holbertonschool.com>


"""Print numbers 0 to 99, two digits each, in ascending order."""
for number in range(0, 100):
    if number == 99:
        print("{}".format(number))
    else:
        print("{:02}".format(number), end=", ")
