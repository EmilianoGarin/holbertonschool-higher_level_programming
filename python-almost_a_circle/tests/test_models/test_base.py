#!/usr/bin/python3
"""Unittest for Base(((Reparar)))
"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """
    test the class Base
    """

    def test_id_none(self):
        self.assertAlmostEqual(Base(None), 1)

    def test_id_empty(self):
        self.assertAlmostEqual(Base(), 2)

    def test_id_not_none(self):
        self.assertAlmostEqual(Base(13), 13)
