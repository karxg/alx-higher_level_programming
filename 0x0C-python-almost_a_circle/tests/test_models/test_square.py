#!/usr/bin/python3
"""
Unit tests for the Square class
"""

import unittest
from io import StringIO
from unittest.mock import patch
from models.rectangle import Rectangle
from models.square import Square


class TestSquareClass(unittest.TestCase):
    """
    Test cases for the Square class
    """

    def test_square_inherited_from_rectangle(self):
        """
        Check if Square class is inherited from Rectangle
        """
        square = Square(10)
        self.assertIsInstance(square, Rectangle)

    def test_arguments_count(self):
        """Test arguments count"""
        with self.assertRaises(TypeError):
            square = Square()
        with self.assertRaises(TypeError):
            square = Square(10, 22, 1, 1, 1, "school")

    def test_size_validation(self):
        """Test size validation"""
        square = Square(10)
        self.assertEqual(square.size, 10)

        square.size = 15
        self.assertEqual(square.size, 15)

        with self.assertRaises(TypeError):
            square.size = "invalid"

        with self.assertRaises(ValueError):
            square.size = -5

    def test_x_validation(self):
        """Test x validation"""
        square = Square(5, 1)
        self.assertEqual(square.x, 1)

        square.x = 15
        self.assertEqual(square.x, 15)

        with self.assertRaises(TypeError):
            square.x = "invalid"

        with self.assertRaises(ValueError):
            square.x = -5

    def test_y_validation(self):
        """Test y validation"""
        square = Square(1, 0, 20)
        self.assertEqual(square.y, 20)

        square.y = 15
        self.assertEqual(square.y, 15)

        with self.assertRaises(TypeError):
            square.y = "invalid"

        with self.assertRaises(ValueError):
            square.y = -5

    def test_area_calculation(self):
        """Test area calculation"""
        square = Square(10)
        self.assertEqual(square.area(), 100)

        square = Square(5)
        self.assertEqual(square.area(), 25)

    def test_display(self):
        """Test display method"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            square = Square(3)
            square.display()
            expected_output = "###\n###\n###\n"
            self.assertEqual(expected_output, fake_out.getvalue())

            with self.assertRaises(TypeError):
                square.display(2)

    def test_display_with_x_y(self):
        """Test display method using x, y"""
        with patch('sys.stdout', new=StringIO()) as fake_out:
            square = Square(2, 3)
            square.display()
            expected_output = "   ##\n   ##\n"
            self.assertEqual(expected_output, fake_out.getvalue())

            square = Square(2, 0, 3)
            square.display()
            expected_output = "\n\n\n##\n##\n"
            self.assertEqual(expected_output, fake_out.getvalue())

            square = Square(3, 2, 2)
            square.display()
            expected_output = "\n\n  ###\n  ###\n  ###\n"
            self.assertEqual(expected_output, fake_out.getvalue())

    def test_display_return_none(self):
        """Test display return"""
        with patch('sys.stdout', new=StringIO()):
            square = Square(3, 2, 2)
            self.assertIsNone(square.display())

    def test_str_representation(self):
        """Test __str__ magic method"""
        square = Square(5, 15, 0, 12)
        self.assertEqual(str(square), "[Square] (12) 15/0 - 5")

        square.x = 5
        square.y = 7
        self.assertEqual(str(square), "[Square] (12) 5/7 - 5")

    def test_update_without_arguments(self):
        """Test update method without arguments"""
        square = Square(5, 10, 0, 10)
        old_size = square.size
        old_x = square.x
        old_y = square.y
        old_id = square.id
        square.update()
        self.assertEqual(old_id, square.id)
        self.assertEqual(old_size, square.size)
        self.assertEqual(old_x, square.x)
        self.assertEqual(old_y, square.y)

    def test_update_with_arguments(self):
        """Test update method with arguments"""
        square = Square(5, 10, 0, 10)
        square.update(1, 2, 3, 4)
        self.assertEqual(1, square.id)
        self.assertEqual(2, square.size)
        self.assertEqual(3, square.x)
        self.assertEqual(4, square.y)

    def test_update_with_args_kwargs(self):
        """Test update method with args and kwargs"""
        square = Square(5, 10, 0, 10)
        square.update(1, id=2)
        self.assertEqual(1, square.id)

        square.update(1, school=2)
        self.assertEqual(1, square.id)

    def test_update_with_kwargs(self):
        """Test update using kwargs"""
        square = Square(10, 10, 10, 10)
        with self.assertRaises(ValueError):
            square.update(school=1)
        old_x = square.x
        old_y = square.y
        square.update(size=1, id=87)
        self.assertEqual(square.id, 87)
        self.assertEqual(square.size, 1)
        self.assertEqual(old_x, square.x)
        self.assertEqual(old_y, square.y)


if __name__ == "__main__":
    unittest.main()
