#!/usr/bin/python3
"""
This module defines a BaseGeometry class with an area method.
"""


class BaseGeometry:
    """
    A class that represents basic geometric shapes.
    """

    def area(self):
        """
        Raises an Exception to indicate that the area method is not
        implemented.

        Raises:
            Exception: Always, with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

