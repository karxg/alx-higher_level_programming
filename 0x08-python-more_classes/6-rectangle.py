#!/usr/bin/python3
"""2-Rectangle module"""


class Rectangle:
    """this is a rectangle class"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing the rectangle class
        Args:
            width: width of the rectangle
            height: height of the rectangle
        Raises:
            TypeError: if size not an integer
            ValueError: if size is less than zero
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """get width"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return self.__height

    @height.setter
    def height(self, value):
        """set height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.height * self.width

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.height == 0 or self.width == 0:
            return 0
        return 2 * (self.height + self.width)

    def __str__(self):
        """returns a rectangle with the character #"""
        if self.height == 0 or self.width == 0:
            return ""
        result = (self.width * "#" + "\n") * (self.height - 1) + (self.width * "#")
        return (result)

    def __repr__(self):
        """returns a rectangle argumentts"""
        return "Rectangle({:d}, {:d})".format(self.width, self.height)

    def __del__(self):
        """prints a delete massage"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
