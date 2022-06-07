#!/usr/bin/python3
""" Unit testing for Base class """

import io
import unittest
import unittest.mock
import sys

h = 'holbertonschool-higher_level_programming/0x0C-python-almost_a_circle'
sys.path.insert(0, f'/home/david/projects/{h}/models')
Base = __import__('base').Base
Rectangle = __import__('rectangle').Rectangle


class TestBase(unittest.TestCase):
    """ Defines unittesting for Base class """
    def test_attribute_incrementation(self):
        """ unittest attribute incrementation """
        new_base = Base()
        self.assertAlmostEqual(new_base._Base__nb_objects, 1)
        self.assertAlmostEqual(new_base.id, 1)
        new_base2 = Base()
        self.assertAlmostEqual(new_base2._Base__nb_objects, 2)
        self.assertAlmostEqual(new_base2.id, 2)
        new_base3 = Base(10)
        self.assertAlmostEqual(new_base3._Base__nb_objects, 2)
        self.assertAlmostEqual(new_base3.id, 10)

    @unittest.mock.patch('sys.stdout', new_callable=io.StringIO)
    def assert_json(self, expected_output, w, h, x, y, mock_stdout):
        """ json test setup """
        rect1 = Rectangle(w, h, x, y)
        dictionary = rect1.to_dictionary()
        json_dictionary = Base.to_json_string(dictionary)
        print(json_dictionary)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_to_json_string(self):
        """ json test """
        e_o = '{"x": 2, "y": 8, "id": 1, "height": 7, "width": 10}\n'
        self.assert_json(e_o, 10, 7, 2, 8)
