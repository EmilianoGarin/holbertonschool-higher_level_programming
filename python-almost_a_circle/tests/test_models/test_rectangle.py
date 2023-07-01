#!/usr/bin/python3
"""Unittest for Rectangle
"""
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestRectangle_init_(unittest.TestCase):
    """
    test the method __init__
    """
    def test_base(self):
        self.assertIsInstance(Rectangle(1, 3), Base)

    def test_one_arg(self):
        with self.assertRaises(TypeError):
            Rectangle(3)

    def test_empty(self):
        with self.assertRaises(TypeError):
            Rectangle()

    def test_full_arg(self):
        a = Rectangle(1, 2, 3, 4, 5)
        b = Rectangle(1, 2, 3, 4, 3)
        self.assertEqual(a.id, b.id + 2)

    def test_not_id_arg(self):
        a = Rectangle(1, 2, 3, 4)
        b = Rectangle(1, 2, 3, 4)
        self.assertEqual(a.id, b.id - 1)

    def test_private_width(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4).__width

    def test_private_height(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4).__height

    def test_private_x(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4).__x

    def test_private_y(self):
        with self.assertRaises(AttributeError):
            Rectangle(1, 2, 3, 4).__y

    def test_init_width_0(self):
        with self.assertRaises(ValueError):
            Rectangle(0, 2, 3, 4)

    def test_init_width_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle("Alice", 2, 3, 4)

    def test_init_height_0(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 0, 3, 4)

    def test_init_height_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(1, "Cheshire", 3, 4)

    def test_init_x_neg(self):
        with self.assertRaises(ValueError):
            Rectangle(1, 2, -3, 4)

    def test_init_x_not_int(self):
        with self.assertRaises(TypeError):
            Rectangle(1, 2, "Madhater", 4)

    def test_init_y_neg(self):
        with self.assertRaises(ValueError):
            a = Rectangle(1, 2, 3, -1)

    def test_init_y_not_int(self):
        with self.assertRaises(TypeError):
            a = Rectangle(1, 2, 3, "white rabbit")


class TestRectangle_getter_and_setter(unittest.TestCase):
    """
    test the method get and set
    """
    def test_get_width(self):
        a = Rectangle(1, 2, 3, 4)
        self.assertEqual(a.width, 1)

    def test_get_height(self):
        a = Rectangle(1, 2, 3, 4)
        self.assertEqual(a.height, 2)

    def test_get_x(self):
        a = Rectangle(1, 2, 3, 4)
        self.assertEqual(a.x, 3)

    def test_get_y(self):
        a = Rectangle(1, 2, 3, 4)
        self.assertEqual(a.y, 4)

    def test_set_width(self):
        a = Rectangle(1, 2, 3, 4)
        a.width = 3
        self.assertEqual(a.width, 3)

    def test_set_width_0(self):
        a = Rectangle(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            a.width = 0

    def test_set_width_not_int(self):
        a = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            a.width = "Alice"

    def test_set_height(self):
        a = Rectangle(1, 2, 3, 4)
        a.height = 3
        self.assertEqual(a.height, 3)

    def test_set_height_0(self):
        a = Rectangle(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            a.height = 0

    def test_set_height_not_int(self):
        a = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            a.height = "Cheshire"

    def test_set_x(self):
        a = Rectangle(1, 2, 3, 4)
        a.x = 1
        self.assertEqual(a.x, 1)

    def test_set_x_neg(self):
        a = Rectangle(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            a.x = -1

    def test_set_x_not_int(self):
        a = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            a.x = "Madhater"

    def test_set_y(self):
        a = Rectangle(1, 2, 3, 4)
        a.y = 1
        self.assertEqual(a.y, 1)

    def test_set_y_neg(self):
        a = Rectangle(1, 2, 3, 4)
        with self.assertRaises(ValueError):
            a.y = -1

    def test_set_y_not_int(self):
        a = Rectangle(1, 2, 3, 4)
        with self.assertRaises(TypeError):
            a.y = "white rabbit"


class TestRectangle_method(unittest.TestCase):
    """
    test the method area
    """

    def test_area(self):
        a = Rectangle(3, 10)
        self.assertAlmostEqual(a.area(), 30)

    """
    test the method display
    """

    def test_display(self):
        a = Rectangle(1, 2, 1, 1)
        self.assertAlmostEqual(a.display(), None)

    """
    test the method update
    """

    def test_args(self):
        a = Rectangle(1, 1)
        a.update(3, 4, 5, 6, 7)
        self.assertAlmostEqual(a.id, 3)
        self.assertAlmostEqual(a.width, 4)
        self.assertAlmostEqual(a.height, 5)
        self.assertAlmostEqual(a.x, 6)
        self.assertAlmostEqual(a.y, 7)

    def test_kwargs(self):
        a = Rectangle(1, 1)
        a.update(width=3, height=4, x=5, y=6, id=7)
        self.assertAlmostEqual(a.id, 7)
        self.assertAlmostEqual(a.width, 3)
        self.assertAlmostEqual(a.height, 4)
        self.assertAlmostEqual(a.x, 5)
        self.assertAlmostEqual(a.y, 6)
