#!/usr/bin/python3
"""
This module provides a function to multiply two matrices using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists): First matrix.
        m_b (list of lists): Second matrix.

    Returns:
        numpy.ndarray: The resulting matrix product.

    Raises:
        TypeError: If m_a or m_b is not a list of lists of integers/floats.
    """
    try:
        return np.matmul(m_a, m_b)
    except ValueError as e:
        raise ValueError("m_a and m_b can't be multiplied") from e
    except TypeError as e:
        raise TypeError("m_a and m_b must be a list of lists") from e
