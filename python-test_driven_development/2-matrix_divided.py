#!/usr/bin/python3
"""
This module provides a function to divide all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): A matrix (list of lists) of integers or floats.
        div (int or float): The number to divide each matrix element by.

    Returns:
        list of lists: A new matrix with each element divided by `div`,
                       rounded to 2 decimal places.

    Raises:
        TypeError: If `matrix` is not a list of lists of integers/floats,
                   if rows are not of the same size, or if `div` is not
                   a number.
        ZeroDivisionError: If `div` is zero.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/"
                        "floats")
    if not all(isinstance(el, (int, float)) for row in matrix for el in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/"
                        "floats")
    if len({len(row) for row in matrix}) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if div == float('inf') or div == -float('inf'):
        return [[0.0 for _ in row] for row in matrix]

    return [[round(el / div, 2) for el in row] for row in matrix]
