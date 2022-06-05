#!/usr/bin/python3
""" Unittesting for Rectangle """

import unittest
import sys

h = 'holbertonschool-higher_level_programming/0x0C-python-almost_a_circle'
sys.path.insert(0, f'/home/david/projects/{h}/models')
Rectangle = __import__('rectangle').Rectangle


class TestRectangle(unittest.TestCase):
    """ Define unittesting for Rectangle """
    def test_defining_attributes(self):
        rect1 = Rectangle(10, 15, 2, 3, 25)
        self.assertAlmostEqual(rect1.width, 10)
        self.assertAlmostEqual(rect1.height, 15)
        self.assertAlmostEqual(rect1.x, 2)
        self.assertAlmostEqual(rect1.y, 3)
        self.assertAlmostEqual(rect1.id, 25)
        rect2 = Rectangle(10, 15)
        self.assertAlmostEqual(rect2.width, 10)
        self.assertAlmostEqual(rect2.height, 15)
        self.assertAlmostEqual(rect2.x, 0)
        self.assertAlmostEqual(rect2.y, 0)
        self.assertAlmostEqual(rect2.id, 1)

    def test_getting_setting(self):
        rect1 = Rectangle(10, 15, 2, 3, 25)
        rect1.width = 20
        rect1.height = 30
        rect1.x = 4
        rect1.y = 6
        self.assertAlmostEqual(rect1.width, 20)
        self.assertAlmostEqual(rect1.height, 30)
        self.assertAlmostEqual(rect1.x, 4)
        self.assertAlmostEqual(rect1.y, 6)
        with self.assertRaises(TypeError):
            rect1.width = "hello"
            rect1.height = 4.9
            rect1.x = (2)
            rect1.y = [3]
        with self.assertRaises(ValueError):
            rect1.width = 0
            rect1.height = -1
            rect1.x = -1
            rect1.y = -5
