#!/usr/bin/python3
# 102-magic_calculation.py
# Brennan D Baraban <375@holbertonschool.com>


def magic_calculation(a, b):
    result = 2
    for i in range(0, 3):
        try:
            if i > a:
                raise Exception('Too far')
            else:
                result += a ** b / i
        except:
            result = b + a
