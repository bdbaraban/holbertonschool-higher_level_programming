#!/usr/bin/python3
# 100-my_calculator.py
# Brennan D Baraban <375@holbertonschool.com>

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    import calculator_1
    import sys

    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    ops = "+-*/"
    if sys.argv[2] not in ops:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    if sys.argv[2] == ops[0]:
        print("{} + {} = {}".format(a, b, calculator_1.add(a, b)))
    elif sys.argv[2] == ops[1]:
        print("{} - {} = {}".format(a, b, calculator_1.sub(a, b)))
    elif sys.argv[2] == ops[2]:
        print("{} * {} = {}".format(a, b, calculator_1.mul(a, b)))
    else:
        print("{} / {} = {}".format(a, b, calculator_1.div(a, b)))
