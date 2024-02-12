#!/usr/bin/python3
"""Unittest for base class
"""
import unittest

from models.base import Base
from models.rectangle import Rectangle
from ast import literal_eval


class TestBase(unittest.TestCase):
    """
    Test cases for the Base class
    """

    def test_incrementing_id(self):
        """
        Test the incrementing of IDs in the Base class
        """
        base_instance_2 = Base()
        self.assertEqual(base_instance_2.id, 1)
        base_instance_1 = Base(25)
        self.assertEqual(base_instance_1.id, 25)
        base_instance_3 = Base()
        self.assertEqual(base_instance_3.id, 2)

    def test_to_json_string(self):
        """
        Test the conversion of dictionary to JSON string
        """
        rectangle = Rectangle(10, 7, 2, 8)

        # Obtain dictionary representation
        dictionary_representation = rectangle.to_dictionary()

        # Convert to JSON string
        json_string = Base.to_json_string([dictionary_representation])

        # Convert JSON string back to dictionary
        json_dictionary = literal_eval(json_string[1: -1])

        # Compare original dictionary with the converted one
        self.assertDictEqual(dictionary_representation, json_dictionary)
