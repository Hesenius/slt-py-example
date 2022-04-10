#!/usr/bin/env python

"""
Author: Nick Russo
File: shape_unittest.py
Purpose: Entrypoint for unittest regression testing of the
circle and rectangle classes.
"""

import unittest

from shapes.circle import Circle
from unittests.rectangle_test import RectangleTest
from unittests.circle_test import CircleTest
from unittests.triangular_test import TriangularTest


def main():
    """
    Test execution starts here.
    """

    # The loader is responsible for loading test cases into test suites
    test_loader = unittest.TestLoader()

    # Build a list of test suites to run
    test_suites = [
        test_loader.loadTestsFromTestCase(CircleTest),
        test_loader.loadTestsFromTestCase(RectangleTest),
        test_loader.loadTestsFromTestCase(TriangularTest)
    ]

    def test_circle():
        """
        Defines tests on some specific circle objects.
        """
        radius5 = Circle(5)
        radius8 = Circle(8)

        # Test areas, perimeters, and diameters
        assert radius5.area() == 78.54
        assert radius8.area() == 201.06
        assert radius5.perimeter() == 31.42
        assert radius8.perimeter() == 50.27
        assert radius5.diameter() == 10
        assert radius8.diameter() == 16

    def test_circle():
        """
        Defines tests on some specific circle objects.
        """
        radius5 = Circle(5)
        radius8 = Circle(8)

        # Test areas, perimeters, and diameters
        assert radius5.area() == 78.54
        assert radius8.area() == 201.06
        assert radius5.perimeter() == 31.42
        assert radius8.perimeter() == 50.27
        assert radius5.diameter() == 10
        assert radius8.diameter() == 16



    # The runner is responsible for executing tests and printing output
    test_runner = unittest.TextTestRunner(verbosity=2)

    # Iterate over all of the test suites, run each one in series
    for test_suite in test_suites:
        test_runner.run(test_suite)


if __name__ == "__main__":
    main()
