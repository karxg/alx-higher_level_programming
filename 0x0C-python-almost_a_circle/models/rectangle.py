#!/usr/bin/python3
"""Rectangle class module"""

from models.base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int): The x-coordinate of the rectangle.
            y (int): The y-coordinate of the rectangle.
            id (int): Optional, the identifier for the instance.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter"""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X-coordinate getter"""
        return self.__x

    @x.setter
    def x(self, value):
        """X-coordinate setter"""
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y-coordinate getter"""
        return self.__y

    @y.setter
    def y(self, value):
        """Y-coordinate setter"""
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Calculate the area of the rectangle."""
        return self.height * self.width

    def display(self):
        """Display the rectangle."""
        rectangle = self.y * "\n" + (self.height * (self.x * " " +
                                                    self.width * "#" + "\n"))
        print(rectangle, end="")

    def update(self, *args, **kwargs):
        """Update the attributes of the rectangle."""
        if args:
            attr_list = ["id", "width", "height", "x", "y"]
            for i, value in enumerate(args):
                if i < len(attr_list):
                    setattr(self, attr_list[i], value)
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
                else:
                    raise ValueError(f"{key} is not attribute in this class")

    def to_dictionary(self):
        """Return the dictionary representation of the rectangle."""
        rectangle_dict = {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
        return rectangle_dict

    def __str__(self):

        """Return the string representation of the rectangle."""
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} " \
            f"- {self.width}/{self.height}"
