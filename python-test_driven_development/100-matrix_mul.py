#!/usr/bin/python3
"""
This module provides a function to multiply two matrices.
"""


def matrix_mul(m_a, m_b):
    """
    Multiplies two matrices (m_a and m_b).

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        list of lists: The resulting matrix product.

    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers/floats.
        ValueError: If m_a or m_b is empty or cannot be multiplied.
    """
    # Validate m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # Validate m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # Validate m_a and m_b are not empty
    if not m_a or not any(m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or not any(m_b):
        raise ValueError("m_b can't be empty")

    # Validate all elements in m_a and m_b are integers or floats
    if not all(isinstance(el, (int, float)) for row in m_a for el in row):
        raise TypeError("m_a should contain only integers or floats")
    if not all(isinstance(el, (int, float)) for row in m_b for el in row):
        raise TypeError("m_b should contain only integers or floats")

    # Validate each row in m_a and m_b is the same size
    if len({len(row) for row in m_a}) > 1:
        raise TypeError("each row of m_a must be of the same size")
    if len({len(row) for row in m_b}) > 1:
        raise TypeError("each row of m_b must be of the same size")

    # Validate m_a and m_b dimensions for multiplication
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication
    result = []
    for row in m_a:
        new_row = []
        for col in range(len(m_b[0])):
            new_row.append(sum(row[i] * m_b[i][col] for i in range(len(m_b))))
        result.append(new_row)

    return result
