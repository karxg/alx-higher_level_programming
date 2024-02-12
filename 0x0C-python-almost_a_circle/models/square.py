#!/usr/bin/python3
"""Square class module"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class representation"""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a Square instance.

        Args:
            size (int): The size of the square.
            x (int): The x-coordinate of the square.
            y (int): The y-coordinate of the square.
            id (int): Optional, the identifier for the instance.
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the string representation of the square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} " \
            f"- {self.height}"

    @property
    def size(self):
        """Size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """Size setter"""
        self.width = value
        self.height = self.width

    def update(self, *args, **kwargs):
        """Update the attributes of the square."""
        if args:
            attr_list = ["id", "size", "x", "y"]
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
        """Return the dictionary representation of the square."""
        square_dict = {
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
        }
        return square_dict
