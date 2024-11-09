#!/usr/bin/python3
"""
This module defines a class BaseGeometry with methods to calculate
area and validate integer values.
"""


class BaseGeometry:
    """
    A class that represents geometry.
    """

    def area(self):
        """
        Raises an Exception to indicate that the area method is not
        implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the value (assumed to be a string).
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer, with a message
            "<name> must be an integer".
            ValueError: If value is less than or equal to 0, with a
            message "<name> must be greater than 0".
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
