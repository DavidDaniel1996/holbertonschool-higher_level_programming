#!/usr/bin/python3
""" Unittesting for Rectangle """

import io
from re import S
import unittest
import unittest.mock
import sys

h = "holbertonschool-higher_level_programming/0x0C-python-almost_a_circle"
sys.path.insert(0, f"/home/david/projects/{h}/models")
Square = __import__('square').Square


class TestSquare(unittest.TestCase):
    """ Define unittesting for Square """
    def test_defining_attributes(self):
        """ unittesting attribute """
        sq1 = Square(20, 2, 3, 25)
        self.assertAlmostEqual(sq1.size, 20)
        self.assertAlmostEqual(sq1.x, 2)
        self.assertAlmostEqual(sq1.y, 3)
        self.assertAlmostEqual(sq1.id, 25)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_str(self, expected_output, s, x, y, id, mock_stdout):
        """ str setup """
        sq1 = Square(s, x, y, id)
        print(sq1)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        """ unittest str """
        self.assert_str("[Square] (12) 2/1 - 10\n", 10, 2, 1, 12)
        self.assert_str("[Square] (1) 0/0 - 5\n", 5, 0, 0, 1)

    def test_getting_setting(self):
        """ unittest getting and setting """
        s1 = Square(20, 2, 3, 25)
        self.assertAlmostEqual(s1.size, 20)
        s1.size = 10
        self.assertAlmostEqual(s1.size, 10)
        with self.assertRaises(TypeError):
            s1.size = "hello"
            s1.size = 2.5
            s1.size = (1)
            s1.size = [3]
        with self.assertRaises(ValueError):
            s1.size = 0
            s1.size = -5

    def test_update(self):
        """ unittest update """
        s1 = Square(20, 25, 2, 3)
        s1.update(30)
        self.assertAlmostEqual(s1.id, 30)
        s1.update(40, 50, 4, 6)
        self.assertAlmostEqual(s1.id, 40)
        self.assertAlmostEqual(s1.size, 50)
        self.assertAlmostEqual(s1.x, 4)
        self.assertAlmostEqual(s1.y, 6)
        s1.update(x=13, y=14)
        self.assertAlmostEqual(s1.x, 13)
        self.assertAlmostEqual(s1.y, 14)
        s1.update(10, x=16)
        self.assertAlmostEqual(s1.id, 10)
        self.assertAlmostEqual(s1.x, 13)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_dictionary(self, expected_output, s, x, y, id, mock_stdout):
        """ setup dictionary """
        sq1 = Square(s, x, y, id)
        dict1 = sq1.to_dictionary()
        print(dict1)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_to_dictionary(self):
        """ unittest dictionary """
        expected_output = "{'id': 1, 'x': 2, 'size': 10, 'y': 1}\n"
        self.assert_dictionary(expected_output, 10, 2, 1, 1)
