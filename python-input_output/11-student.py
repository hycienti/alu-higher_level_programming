#!/usr/bin/python3
"""
This module defines a Student class with attributes and methods
for JSON serialization and deserialization.
"""


class Student:
    """
    Defines a student with first name, last name, and age.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        If `attrs` is a list of strings, only the attributes in the list
        are included. Otherwise, all attributes are included.

        Args:
            attrs (list): Optional list of attribute names to include.

        Returns:
            dict: The dictionary representation of the instance.
        """
        if isinstance(attrs, list) and all(
            isinstance(attr, str) for attr in attrs
        ):
            return {
                key: getattr(self, key)
                for key in attrs if hasattr(self, key)
            }
        return self.__dict__

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance with values
        from the given dictionary.

        Args:
            json (dict): A dictionary containing attribute names and values
                         to replace the current attributes.
        """
        for key, value in json.items():
            setattr(self, key, value)
