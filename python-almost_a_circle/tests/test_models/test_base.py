#!/usr/bin/python3
"""Unittest for Base
"""
import unittest
from models.base import Base


class TestBase_init_(unittest.TestCase):
    """
    test the method __init__
    """

    def test_id_none(self):
        self.assertAlmostEqual(Base(None).id, 4)

    def test_id_empty(self):
        self.assertAlmostEqual(Base().id, 1)

    def test_id_not_none(self):
        self.assertAlmostEqual(Base(13).id, 13)

    def test_id_neg(self):
        self.assertAlmostEqual(Base(-1).id, -1)

    def test_id_0(self):
        self.assertAlmostEqual(Base(0).id, 0)

    def test_id_multiple(self):
        i = Base()
        x = Base()
        self.assertAlmostEqual(x.id, i.id + 1)


class TestBase_JSON(unittest.TestCase):
    """
    test method that use JSON
    """

    def test_json_string_none(self):
        self.assertAlmostEqual(Base.to_json_string(None), "[]")

    def test_json_string_not_none(self):
        res = '["Alice"]'
        data = ['Alice']
        self.assertAlmostEqual(Base.to_json_string(data), res)

    def test_json_file_s_none(self):
        self.assertEqual(Base.save_to_file(None), None)

    def test_json_file_f_none(self):
        self.assertEqual(Base.from_json_string(None), [])

    def test_json_file_l_empty(self):
        self.assertEqual(Base.load_from_file(), [])
