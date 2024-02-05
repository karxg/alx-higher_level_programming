#!/usr/bin/python3
"""
Defines a base geometry class, BaseGeometry, with an unimplemented area method
"""


class BaseGeometry:
    """Represents the base geometry class.

    Methods:
        area(self): Placeholder for calculating the area.
    """
    def area(self):
        """Not implemented."""
        raise Exception("area() is not implemented")
