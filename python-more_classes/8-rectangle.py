#!/usr/bin/python3
"""
This module defines a Rectangle class that represents a rectangle shape.

The Rectangle class has attributes for width and height, and provides
methods to calculate area and perimeter, print the rectangle, compare
rectangles by area, and track the number of instances.
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
