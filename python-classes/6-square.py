#!/usr/bin/python3
"""
Defines a Square class with size and position validation, and methods for
area calculation and printing.
"""


class Square:
    """
    This class defines a square with private instance attributes size and
    position.

    Attributes:
    size (int): The size of the square's side (must be a non-negative integer).
    position (tuple): A tuple of 2 positive integers specifying the position
    of the square.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance with private size and position
        attributes.

        Parameters:
        size (int): The size of the square (default is 0).
        position (tuple): The position of the square (default is (0, 0)).

        Raises:
        TypeError: If size is not an integer or position is not a tuple of
                   2 positive integers.
        ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves the size of the square."""
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

    @property
    def position(self):
        """Retrieves the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets the position of the square with validation.

        Parameters:
        value (tuple): A tuple of 2 positive integers for the square's position.

        Raises:
        TypeError: If value is not a tuple of 2 positive integers.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates and returns the area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square using the character '#'.

        If size is 0, prints an empty line.
        The position is used to print leading spaces and newlines as specified.
        """
        if self.__size == 0:
            print("")
            return

        # Print the vertical spacing (position[1])
        for _ in range(self.__position[1]):
            print("")

        # Print each line of the square with leading spaces
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)
