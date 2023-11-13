#!/usr/bin/python3
"""module Rectangle.
Create a Rectangle class that inherits from Base.
"""
import json
from models.base import Base


class Rectangle(Base):
    """class describing rectangle
    public instance method:
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializes a rectangle instance.
        Args:
        -__width: width
        - __height: height
        - __x: position
        - __y: position
        - id: id
        """

        self.height = height
        self.width = width
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """retrieves the width attribibute."""
        return self.__width

    @property
    def height(self):
        """retrieves the height attribute."""
        return self.__height

    @property
    def x(self):
        """retrieves the x attribute."""
        return self.__x

    @property
    def y(self):
        """retrieves the y attribute."""
        return self.__y

    @width.setter
    def width(self, value):
        """sets the width attribute"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """sets the height attribute"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """sets the x attribute"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """sets the y attribute"""

        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """calculates the area of rectange instance
        Returns: area
        """

        return self.__width*self.__height

    def display(self):
        """print the rectangle instance with # character"""

        for y in range(0, self.__y):
            print()
        for i in range(0, self.__height):
            for x in range(0, self.__x):
                print(" ", end="")
            for j in range(0, self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """Returns a string respresentation of a rectangle instance."""

        s = "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)
        return s

    def update(self, *args, **kwargs):
        """"updates attribute of an instance"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                if type(args[0]) != int and args[0] is not None:
                    raise TypeError("id must be an integer")
                self.id = args[0]
                if len(args) > 1:
                    self.width = args[1]
                if len(args) > 2:
                    self.height = args[2]
                if len(args) > 3:
                    self.x = args[3]
                if len(args) > 4:
                    self.y = args[4]
            else:
                for key, value in kwargs.items():
                    if key == "id":
                        if type(value) != int and value is not None:
                            raise TypeError("id must be an integer")
                        self.id = value
                    if key == "width":
                        self.width = value
                    if key == "height":
                        self.height = value
                    if key == "x":
                        self.x = value
                    if key == "y":
                        self.y = value

    def to_dictionary(self):
        """Returns the dictionary representation of a Rectangle."""
        my_dict = {'id': self.id, 'width': self.__width,
                   'height': self.__height, 'x': self.__x, 'y': self.__y}
        return my_dict
