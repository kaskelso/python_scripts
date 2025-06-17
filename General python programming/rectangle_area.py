#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 14:38:17 2024

@author: kennyaskelson
"""

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.id = "Rectangle"
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return ((2 * self.width) + (2 * self.height))
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** .5)
    def __str__(self):
        return f"{self.id}(width={self.width}, height={self.height})"
    def get_picture(self):
        picture = ""
        if self.height > 50:
            return "Too big for picture."
        elif self.width > 50:
            return "Too big for picture."
        else:
            for i in range(self.height):
                picture += "*" * self.width + "\n"
            return picture
    def get_amount_inside(self, shape):
        if not isinstance(shape, (Rectangle, Square)):
            raise ValueError("Argument must be a Rectangle or Square")

        return self.get_area() // shape.get_area()
        

class Square(Rectangle):
    def __init__(self, side_length):
        # Call the __init__ method of the parent class (Rectangle)
        super().__init__(side_length, side_length)
        self.id = "Square"
    def set_side(self, side_length):
        # Use the inherited set_width and set_height methods
        self.set_width(side_length)
        self.set_height(side_length)
    def __str__(self):
        return f"{self.id}(side={self.width})"
    def set_width(self, width):
        self.width = width
        self.height = width
    def set_height(self, height):
        self.width = height
        self.height = height