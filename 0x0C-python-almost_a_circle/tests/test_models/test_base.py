#!/usr/bin/python3
""" Unit testing for Base class """

import unittest
import sys

h = 'holbertonschool-higher_level_programming/0x0C-python-almost_a_circle'
sys.path.insert(0, f'/home/david/projects/{h}/models')
Base = __import__('base').Base


class TestBase(unittest.TestCase):
    """ Defines unittesting for Base class """
    def test_attribute_incrementation(self):
        """ creates 3 objects and tests for __nb_objects and id attributes """
        new_base = Base()
        self.assertAlmostEqual(new_base._Base__nb_objects, 1)
        self.assertAlmostEqual(new_base.id, 1)
        new_base2 = Base()
        self.assertAlmostEqual(new_base2._Base__nb_objects, 2)
        self.assertAlmostEqual(new_base2.id, 2)
        new_base3 = Base(10)
        self.assertAlmostEqual(new_base3._Base__nb_objects, 2)
        self.assertAlmostEqual(new_base3.id, 10)
