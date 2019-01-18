#!/usr/bin/python3
# 101-stats.py
# Brennan D Baraban <375@holbertonschool.com>
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

size = 0
status_codes = {}

while True:
    for i in range(10):
        line = input()
        line = line.split()

        size += int(line[8])
        if status_codes.get(line[7], -1) == -1:
            status_codes[line[7]] = 1
        else:
            status_codes[line[7]] += 1

    print("File size: {}".format(size))
    for key in sorted(status_codes):
        print("{}: {}".format(key, status_codes[key]))
