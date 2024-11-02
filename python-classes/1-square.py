#!/usr/bin/python3
"""
This module defines a Square class with a private size attribute.
"""


class Square:
    """
    This class defines a square with a private instance attribute size.
    """
    def __init__(self, size):
        """
        Initializes a new Square instance with a private size attribute.

        Parameters:
        size: The size of the square (no type or value validation).
        """
        self.__size = size
