#!/usr/bin/python3
# 6-print_matrix_integer.py
# Brennan D Baraban <375@holbertonschool.com>


def print_matrix_integer(matrix=[[]]):
    """Print a matrix of integers."""
    if isinstance(matrix, list) == False:
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
                print("{:d}".format(matrix[i][j]), end="")
                if j != 2:
                    print(" ", end="")

        print("")
