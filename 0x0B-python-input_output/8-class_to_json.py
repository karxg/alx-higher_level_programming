#!/usr/bin/python3
"""Class to JSON Module"""


def class_to_json(obj):
    """Converts a Python class instance to a dictionary representation.

    Args:
        obj: The Python class instance to be converted.

    Returns:
        dict: The dictionary representation of the input Python class instance.
    """
    return obj.__dict__
