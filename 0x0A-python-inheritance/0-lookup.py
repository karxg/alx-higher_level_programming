#!/usr/bin/python3
"""Defines a function for listing attributes of an object."""


def lookup(obj):
    """Return a list of attributes available for the given object."""
    return dir(obj)
