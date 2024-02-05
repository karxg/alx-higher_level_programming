#!/usr/bin/python3
"""
Defines a base geometry class, BaseGeometry, with methods for area
calculation and integer validation.
"""


class BaseGeometry:
    """Represents the base geometry class.

    Methods:
        area(self): Placeholder for calculating the area.
        integer_validator(self, name, value): Validates a parameter
        as an integer

    Raises:
        TypeError: If value is not an integer.
        ValueError: If value is <= 0.
    """
    def area(self):
        """Not yet implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate a parameter as an integer.

        Args:
            name (str): The name of the parameter.
            value (int): The parameter to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is <= 0.
        """
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
