#!/usr/bin/env python

"""
Author: Franz Hesenius
Purpose: Defines a triangular object, inherited from the abstract class Shape.
"""
import math

from shapes.shape import Shape


class Triangular(Shape):
    """
    Represents a Triangular shape, and contains the length of two sides of a triangle
    and the size of the including angle these sides generate
    """

    def __init__(self, length_side1, lengt_side2, angle):
        self.length_side1 = length_side1
        self.length_side2 = lengt_side2
        self.angle = angle
        self.radian = math.radians(angle)

    def area(self):
        """
        Compute the area using the formula (side1 * side2 * sinus(angle))/2
        """

        return (self.length_side1 * self.length_side2 * math.sin(self.radian)) / 2

    def perimeter(self):
        """
        Compute the perimeter using the formula law of cosines to calculate the unknown side3.
        side3 = side1 ** 2 + side 2 ** 2 - 2(side1 * side2) * cos (angel)
        The perimeter is then side1 + side2 + side3

        """
        side3 = self.length_side1 ** 2 + self.length_side2 ** 2 - \
                2 * (self.length_side1 * self.length_side2) * math.cos(self.radian)
        return self.length_side1 + self.length_side2 + side3
