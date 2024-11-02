#!/usr/bin/python3
"""
Defines a Square class with size validation, a getter, and methods for area and printing.
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
        self.size = size  # Using the property setter for validation

    @property
    def size(self):
        """
        Retrieves the size of the square.

        Returns:
        int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets the size of the square with validation.

        Parameters:
        value (int): The new size of the square.

        Raises:
        TypeError: If value is not an integer.
        ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates and returns the area of the square.

        Returns:
        int: The area of the square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using the character '#'.

        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
