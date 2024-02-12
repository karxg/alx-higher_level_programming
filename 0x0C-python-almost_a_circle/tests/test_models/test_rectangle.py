#!/usr/bin/python3
"""
Unit tests for the Rectangle class
"""

import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.base import Base


class TestRectangleClass(unittest.TestCase):
    """
    Test cases for the Rectangle class
    """

    def test_rectangle_inherited_from_base(self):
        """
        Check if Rectangle class is inherited from Base
        """
        rectangle = Rectangle(10, 20)
        self.assertIsInstance(rectangle, Base)

    def test_arguments_count(self):
        """Test arguments count"""
        with self.assertRaises(TypeError):
            rect = Rectangle()
        with self.assertRaises(TypeError):
            rect = Rectangle(10, 22, 1, 1, 1, "school")

    def test_width_validation(self):
        """Test width validation"""
        rect = Rectangle(10, 5)
        self.assertEqual(rect.width, 10)

        rect.width = 15
        self.assertEqual(rect.width, 15)

        with self.assertRaises(TypeError):
            rect.width = "invalid"

        with self.assertRaises(ValueError):
            rect.width = -5

    def test_height_validation(self):
        """Test height validation"""
        rect = Rectangle(10, 5)
        self.assertEqual(rect.height, 5)

        rect.height = 15
        self.assertEqual(rect.height, 15)

        with self.assertRaises(TypeError):
            rect.height = "invalid"

        with self.assertRaises(ValueError):
            rect.height = -5

    def test_x_validation(self):
        """Test x validation"""
        rect = Rectangle(10, 5, 1)
        self.assertEqual(rect.x, 1)

        rect.x = 15
        self.assertEqual(rect.x, 15)

        with self.assertRaises(TypeError):
            rect.x = "invalid"

        with self.assertRaises(ValueError):
            rect.x = -5

    def test_y_validation(self):
        """Test y validation"""
        rect = Rectangle(10, 5, 1, 20)
        self.assertEqual(rect.y, 20)

        rect.y = 15
        self.assertEqual(rect.y, 15)

        with self.assertRaises(TypeError):
            rect.y = "invalid"

        with self.assertRaises(ValueError):
            rect.y = -5

    def test_area_calculation(self):
        """Test area calculation"""
        rect = Rectangle(10, 5)
        self.assertEqual(rect.area(), 50)

        rect = Rectangle(5, 10)
        self.assertEqual(rect.area(), 50)

    def test_display(self):
        """Test display method"""
        # Mocking stdout to test output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle = Rectangle(2, 3)
            rectangle.display()
            expected_output = "##\n##\n##\n"
            self.assertEqual(expected_output, fake_out.getvalue())

            rectangle = Rectangle(3, 2)
            rectangle.display()
            expected_output = "###\n###\n"
            self.assertEqual(expected_output, fake_out.getvalue())

            rectangle.width = 3
            rectangle.height = 3
            rectangle.display()
            expected_output = "###\n###\n###\n"
            self.assertEqual(expected_output, fake_out.getvalue())

            with self.assertRaises(TypeError):
                rectangle.display(2)

    def test_display_with_x_y(self):
        """Test display method using x, y"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            rectangle = Rectangle(2, 3, 3, 0)
            rectangle.display()
            expected_output = "   ##\n   ##\n   ##\n"
            self.assertEqual(expected_output, fake_out.getvalue())

            rectangle = Rectangle(3, 2, 0, 3)
            rectangle.display()
            expected_output = "\n\n\n###\n###\n"
            self.assertEqual(expected_output, fake_out.getvalue())

            rectangle = Rectangle(3, 2, 2, 3)
            rectangle.display()
            expected_output = "\n\n\n  ###\n  ###\n"
            self.assertEqual(expected_output, fake_out.getvalue())

    def test_display_return_none(self):
        """Test display return"""
        with patch('sys.stdout', new=StringIO()):
            rectangle = Rectangle(3, 2, 2, 3)
            self.assertIsNone(rectangle.display())

    def test_str_representation(self):
        """Test __str__ magic method"""
        rectangle = Rectangle(5, 15, 0, 0, 12)
        self.assertEqual(str(rectangle), "[Rectangle] (12) 0/0 - 5/15")

        rectangle.x = 5
        rectangle.y = 7
        self.assertEqual(str(rectangle), "[Rectangle] (12) 5/7 - 5/15")

    def test_update_without_arguments(self):
        """Test update method without arguments"""
        rectangle = Rectangle(5, 10, 0, 10, 5)
        old_height = rectangle.height
        old_width = rectangle.width
        old_x = rectangle.x
        old_y = rectangle.y
        old_id = rectangle.id
        rectangle.update()
        self.assertEqual(old_id, rectangle.id)
        self.assertEqual(old_height, rectangle.height)
        self.assertEqual(old_width, rectangle.width)
        self.assertEqual(old_x, rectangle.x)
        self.assertEqual(old_y, rectangle.y)

    def test_update_with_arguments(self):
        """Test update method with arguments"""
        rectangle = Rectangle(5, 10, 0, 10, 5)
        rectangle.update(1, 2, 3, 4, 5)
        self.assertEqual(1, rectangle.id)
        self.assertEqual(2, rectangle.width)
        self.assertEqual(3, rectangle.height)
        self.assertEqual(4, rectangle.x)
        self.assertEqual(5, rectangle.y)

    def test_update_with_args_kwargs(self):
        """Test update method with args and kwargs"""
        rectangle = Rectangle(5, 10, 0, 10, 5)
        rectangle.update(1, id=2)
        self.assertEqual(1, rectangle.id)

        rectangle.update(1, school=2)
        self.assertEqual(1, rectangle.id)

    def test_update_with_kwargs(self):
        """Test update using kwargs"""
        rectangle = Rectangle(10, 10, 10, 10, 5)
        with self.assertRaises(ValueError):
            rectangle.update(school=1)
        old_height = rectangle.height
        old_x = rectangle.x
        old_y = rectangle.y
        rectangle.update(width=1, id=87)
        self.assertEqual(rectangle.id, 87)
        self.assertEqual(old_height, rectangle.height)
        self.assertEqual(rectangle.width, 1)
        self.assertEqual(old_x, rectangle.x)
        self.assertEqual(old_y, rectangle.y)

    def test_to_dictionary_method(self):
        """Test to_dictionary method"""
        rectangle = Rectangle(1, 2, 3, 4, 5)
        expected_rect_dict = {'height': 2, 'id': 5, 'width': 1, 'x': 3, 'y': 4}
        self.assertDictEqual(rectangle.to_dictionary(), expected_rect_dict)

        with self.assertRaises(TypeError):
            rectangle.to_dictionary(2)


if __name__ == "__main__":
    unittest.main()
