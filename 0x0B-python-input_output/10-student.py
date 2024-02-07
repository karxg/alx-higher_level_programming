#!/usr/bin/python3
"""Student Module"""


class Student:
    """A class representing a student."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Converts the Student object to a JSON-compatible dictionary.

        Args:
            attrs (list of str, optional): The attributes to include in the
                dictionary representation. If not provided, all attributes
                will be included.

        Returns:
            dict: A dictionary representation of the Student object.
        """
        attr_dict = self.__dict__
        if attrs is None:
            return attr_dict

        new_dict = {}
        for key in attrs:
            value = attr_dict.get(key)
            if value:
                new_dict[key] = value
        return new_dict
