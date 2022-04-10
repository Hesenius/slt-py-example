"""
Author: Franz Hesenius
File: triangular_test.py
Purpose: Unit tests for the Circle class.
"""

from unittest import TestCase

from shapes.triangular import Triangular


class TriangularTest(TestCase):
    """
    Defines a test case for the Triangular class.
    """

    def setUp(self):
        """
        Create a few test objects.
        """
        self.triangular1 = Triangular(5,4,30)
        self.triangular2 = Triangular(7, 9, 60)
        self.triangular3 = Triangular(6, 4, 90)

    def test_area(self):
        """
        Compare the test triangular area computations to the actual values.
        """
        self.assertEqual(self.triangular1.area(), 78.54)
        self.assertEqual(self.triangular2.area(), 201.06)

    def test_perimeter(self):
        """
        Compare the test triangular perimeter computations to the actual values.
        """
        self.assertEqual(self.triangular3.perimeter(), 31.42)
        self.assertEqual(self.triangular2perimeter(), 50.27)

