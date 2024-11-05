#!/usr/bin/python3
"""
This module defines a Rectangle class representing a rectangle shape.
"""


class Rectangle:
    """
    Defines a rectangle with width, height, and instance tracking.
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialize a new Rectangle.

        Args:
            width (int): Rectangle width, defaults to 0.
            height (int): Rectangle height, defaults to 0.
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Get the width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width, ensuring it's a non-negative int."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Get the height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height, ensuring it's a non-negative int."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        Calculate area of the rectangle.

        Returns:
            int: The area.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculate perimeter.

        Returns:
            int: Perimeter, or 0 if width or height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        Return a string using `print_symbol`.

        Returns:
            str: Rectangle as `print_symbol`, or empty if width/height is 0.
        """
        if self.__width == 0 or self.__height == 0:
            return ""
        return "\n".join([
            str(self.print_symbol) * self.__width for _ in range(self.__height)
        ])

    def __repr__(self):
        """
        Return a string to recreate the instance.

        Returns:
            str: A string representation for eval().
        """
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Print message and decrement instance counter."""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Return the rectangle with the bigger area, or rect_1 if equal.

        Args:
            rect_1 (Rectangle): The first rectangle.
            rect_2 (Rectangle): The second rectangle.

        Returns:
            Rectangle: The rectangle with the larger area or rect_1 if equal.

        Raises:
            TypeError: If rect_1 or rect_2 is not an instance of Rectangle.
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Create a new Rectangle instance with width == height == size.

        Args:
            size (int): The side length of the square.

        Returns:
            Rectangle: New rectangle instance with equal width and height.
        """
        return cls(size, size)
