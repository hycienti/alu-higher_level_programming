#!/usr/bin/python3
"""
This module defines a class BaseGeometry with an unimplemented area method.
"""


class BaseGeometry:
    """
    A class that represents geometry.
    """

    def area(self):
        """
        Raises an Exception to indicate that the area method is not implemented.
        """
        raise Exception(
            "area() is not implemented"
        )
