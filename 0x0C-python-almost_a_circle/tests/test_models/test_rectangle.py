#!/usr/bin/python3
""" Unittesting for Rectangle """

import io
import unittest
import unittest.mock
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

    def test_area(self):
        rect1 = Rectangle(10, 15, 2, 3, 25)
        my_area = rect1.area()
        self.assertAlmostEqual(my_area, 150)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_display(self, expected_output, w, h, x, y, mock_stdout):
        rect1 = Rectangle(w, h, x, y)
        rect1.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display(self):
        self.assert_display("\n ##\n ##\n", 2, 2, 1, 1)
        self.assert_display("#\n", 1, 1, 0, 0)
        self.assert_display("  ###\n  ###\n", 3, 2, 2, 0)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_str(self, expected_output, w, h, x, y, id, mock_stdout):
        rect1 = Rectangle(w, h, x, y, id)
        print(rect1)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        self.assert_str("[Rectangle] (12) 2/1 - 4/6\n", 4, 6, 2, 1, 12)
        self.assert_str("[Rectangle] (1) 0/0 - 5/5\n", 5, 5, 0, 0, 1)

    def test_update(self):
        rect1 = Rectangle(10, 15, 2, 3, 25)
        rect1.update(30)
        self.assertAlmostEqual(rect1.id, 30)
        rect1.update(40, 12, 17, 4, 6)
        self.assertAlmostEqual(rect1.id, 40)
        self.assertAlmostEqual(rect1.width, 12)
        self.assertAlmostEqual(rect1.height, 17)
        self.assertAlmostEqual(rect1.x, 4)
        self.assertAlmostEqual(rect1.y, 6)
        rect1.update(width=10, height=11)
        self.assertAlmostEqual(rect1.width, 10)
        self.assertAlmostEqual(rect1.height, 11)
        rect1.update(10, width=20)
        self.assertAlmostEqual(rect1.id, 10)
        self.assertAlmostEqual(rect1.width, 10)
