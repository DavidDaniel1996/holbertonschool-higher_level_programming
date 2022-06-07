#!/usr/bin/python3
""" Unittesting for Rectangle """

import io
import unittest
import unittest.mock
import sys

h = "holbertonschool-higher_level_programming/0x0C-python-almost_a_circle"
sys.path.insert(0, f"/home/david/projects/{h}/models")
Square = __import__('square').Square


class TestSquare(unittest.TestCase):
    """ Define unittesting for Square """
    def test_defining_attributes(self):
        sq1 = Square(20, 2, 3, 25)
        self.assertAlmostEqual(sq1.size, 20)
        self.assertAlmostEqual(sq1.x, 2)
        self.assertAlmostEqual(sq1.y, 3)
        self.assertAlmostEqual(sq1.id, 25)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_str(self, expected_output, s, x, y, id, mock_stdout):
        sq1 = Square(s, x, y, id)
        print(sq1)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_str(self):
        self.assert_str("[Square] (12) 2/1 - 10\n", 10, 2, 1, 12)
        self.assert_str("[Square] (1) 0/0 - 5\n", 5, 0, 0, 1)
