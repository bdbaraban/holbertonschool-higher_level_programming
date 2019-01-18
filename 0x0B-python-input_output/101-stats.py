#!/usr/bin/python3
# 101-stats.py
# Brennan D Baraban <375@holbertonschool.com>
"""Reads from standard input and computes metrics.

After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

if __name__ == "__main__":
    import sys

    size = 0
    status_codes = {}

    while True:
        try:
            count = 0
            for line in sys.stdin:
                line = line.split()

                size += int(line[8])
                if status_codes.get(line[7], -1) == -1:
                    status_codes[line[7]] = 1
                else:
                    status_codes[line[7]] += 1

                if count == 10:
                    break
                count += 1
        except KeyboardInterrupt:
            exit()
        finally:
            print("File size: {}".format(size))
            for key in sorted(status_codes):
                print("{}: {}".format(key, status_codes[key]))
