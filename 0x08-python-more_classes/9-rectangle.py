#!/usr/bin/python3


"""
This module describes a rectangle and all its properties
stay tuned for developments
"""


class Rectangle:
    """
    This is the class rectangle that I told you about
    """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        This is the initializer for the rectangle property
        we are taking the width and the height
        """
        Rectangle.number_of_instances += 1
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if width < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = width
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if height < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = height

    @property
    def width(self):
        """
        retrieve the width of rectangle
        """
        return (self._Rectangle__width)

    @width.setter
    def width(self, value):
        """
        This is where we give a new width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self._Rectangle__width = value

    @property
    def height(self):
        """
        This property is to retrive the height
        """
        return (self._Rectangle__height)

    @height.setter
    def height(self, value):
        """
        Now we need a new height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self._Rectangle__height = value

    def area(self):
        """
        Returns the area of the rectangle
        """
        return (self._Rectangle__width * self._Rectangle__height)

    def perimeter(self):
        """
        Returns thr perimeter of the rectangle
        """
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return (0)
        return (2 * (self._Rectangle__width + self._Rectangle__height))

    def __str__(self):
        """
        Behavoiral trait of recatngle instance
        """
        string = ""
        if self._Rectangle__width == 0 or self._Rectangle__height == 0:
            return (string)
        for y in range(self._Rectangle__height):
            for x in range(self._Rectangle__width):
                string = string + str(self.print_symbol)
            if y != self._Rectangle__height - 1:
                string = string + '\n'
        return (string)

    def __repr__(self):
        """
        This is a developer friendly of my class
        """
        return ("Rectangle({}, {})".format(
            self._Rectangle__width, self._Rectangle__height))

    def __del__(self):
        """
        What will happen when we delete ...
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        compares two Rectangle instance
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        return (rect_1 if rect_1.area() >= rect_2.area() else rect_2)

    @classmethod
    def square(cls, size=0):
        """
        This is creating a square from the rectangle
        """
        return (cls(size, size))
