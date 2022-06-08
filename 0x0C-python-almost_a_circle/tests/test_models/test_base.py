#!/usr/bin/python3
""" Unit testing for Base class """

import io
import unittest
import unittest.mock
import sys

from models.base import Base
from models.rectangle import Rectangle


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
    def assert_json(self, expected_output, dictionary, mock_stdout):
        """ json test setup """
        json_dictionary = Base.to_json_string(dictionary)
        print(json_dictionary)
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_to_json_string(self):
        """ json test """
        rect1 = Rectangle(10, 7, 2, 8)
        dictionary = rect1.to_dictionary()
        e_o = '{"x": 2, "y": 8, "id": 3, "height": 7, "width": 10}\n'
        self.assert_json(e_o, dictionary)
        self.assert_json("[]\n", None)
        self.assert_json("[]\n", {})

if __name__ == '__main__':
    unittest.main()
