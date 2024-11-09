#!/usr/bin/python3
"""
Defines a Square class with size and position validation, and methods
for area calculation and printing.
"""


class Square:
    """
    Defines a square with private size and position attributes.

    Attributes:
    size (int): Size of the square's side (non-negative integer).
    position (tuple): Tuple of 2 positive integers specifying position.
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a new Square instance with size and position.

        Args:
        size (int): Size of the square (default 0).
        position (tuple): Position of the square (default (0, 0)).

        Raises:
        TypeError: If size is not an integer or position is invalid.
        ValueError: If size is less than 0.
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieves size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Sets size of the square with validation.

        Args:
        value (int): New size of the square.

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
        """Retrieves position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """
        Sets position of the square with validation.

        Args:
        value (tuple): Tuple of 2 positive integers for position.

        Raises:
        TypeError: If value is not a valid tuple.
        """
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Calculates area of the square."""
        return self.__size * self.__size

    def my_print(self):
        """
        Prints the square with '#' characters. If size is 0, prints
        an empty line. Uses position for leading spaces.
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
