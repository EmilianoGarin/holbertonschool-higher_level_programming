#!/usr/bin/python3
import unittest
from models.square import Square
from models.rectangle import Rectangle


class TestSquare_init_(unittest.TestCase):
    """
    test the method __init__
    """
    def test_base(self):
        self.assertIsInstance(Square(3), Rectangle)

    def test_empty(self):
        with self.assertRaises(TypeError):
            Square()

    def test_full_arg(self):
        a = Square(2, 3, 4, 5)
        b = Square(2, 3, 4, 3)
        self.assertEqual(a.id, b.id + 2)

    def test_not_id_arg(self):
        a = Square(2, 3, 4)
        b = Square(2, 3, 4)
        self.assertEqual(a.id, b.id - 1)


class TestSquare_getter_and_setter(unittest.TestCase):
    """
    test the method get and set
    """

    def test_get_size(self):
        a = Square(1)
        self.assertEqual(a.size, 1)

    def test_set_size(self):
        a = Square(3)
        a.size = 1
        self.assertEqual(a.size, 1)


class TestSquare_method(unittest.TestCase):
    """
    test the method area
    """

    def test_area(self):
        a = Square(3)
        self.assertAlmostEqual(a.area(), 9)

    """
    test the method display
    """

    def test_display(self):
        a = Square(1, 1, 2)
        self.assertAlmostEqual(a.display(), None)

    """
    test the method update
    """

    def test_args(self):
        a = Square(1)
        a.update(3, 4, 5, 6)
        self.assertAlmostEqual(a.id, 3)
        self.assertAlmostEqual(a.size, 4)
        self.assertAlmostEqual(a.width, 4)
        self.assertAlmostEqual(a.height, 4)
        self.assertAlmostEqual(a.x, 5)
        self.assertAlmostEqual(a.y, 6)

    def test_kwargs(self):
        a = Square(1)
        a.update(size=3, x=5, y=6, id=7)
        self.assertAlmostEqual(a.id, 7)
        self.assertAlmostEqual(a.size, 3)
        self.assertAlmostEqual(a.width, 3)
        self.assertAlmostEqual(a.height, 3)
        self.assertAlmostEqual(a.x, 5)
        self.assertAlmostEqual(a.y, 6)
