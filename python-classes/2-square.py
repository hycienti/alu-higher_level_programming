#!/usr/bin/python3
"""
Defines a Square class with a private size attribute and validation.
"""


class Square:
    """
    This class defines a square with a private instance attribute size.

    Attributes:
    size (int): The size of the square's side (must be a non-negative integer).
    """

    def __init__(self, size=0):
        """
        Initializes a new Square instance with a private size attribute.

        Parameters:
        size (int): The size of the square (default is 0).

        Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
