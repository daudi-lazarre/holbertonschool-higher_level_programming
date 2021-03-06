#!/usr/bin/python3
""" Insert prototype here """


def matrix_divided(matrix, div):
    """ This function divides the numbers in a matrix"""

    if not isinstance(matrix, (int, float)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) != len(matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    quotient = matrix / div

    return(round(quotient, 2))
