#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    test max_integer
    """

    def test_empty_arg(self):
        self.assertAlmostEqual(max_integer(), None)

    def test_empty_list(self):
        self.assertAlmostEqual(max_integer([]), None)

    def test_standard_in(self):
        self.assertAlmostEqual(max_integer([3, 4, 5]), 5)

    def test_standard_mix(self):
        self.assertAlmostEqual(max_integer([5, 3, 4]), 5)

    def test_standard_single(self):
        self.assertAlmostEqual(max_integer([3]), 3)

    def test_standard_neg(self):
        self.assertAlmostEqual(max_integer([-4, -6, -5]), -4)

    def test_standard_random(self):
        self.assertAlmostEqual(max_integer([1, 20, 130, 90]), 130)

    def test_1000000(self):
        big = [0] * 1000000
        self.assertAlmostEqual(max_integer(big), 0)
