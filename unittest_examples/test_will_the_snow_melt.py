# -*- coding: utf-8 -*-
import unittest

from unittest_examples.will_the_snow_melt_1 import will_the_snow_melt_today as version_1
from unittest_examples.will_the_snow_melt_2 import will_the_snow_melt_today as version_2
from unittest_examples.will_the_snow_melt_3 import will_the_snow_melt_today as version_3


class TestWillTheSnowMelt1(unittest.TestCase):
    def test_snow_melts_above_three_degrees(self):
        answer = version_1('5')
        self.assertEqual("It probably will.", answer)

    def test_snow_does_not_melt_below_three_degrees(self):
        answer = version_1('0')
        self.assertEqual("Nope! It's here to stay.", answer)

    def test_non_number_confuses_the_function(self):
        answer = version_1('lumi')
        self.assertEqual("I don't know what that means!", answer)


class TestWillTheSnowMelt2(unittest.TestCase):
    def test_snow_melts_above_three_degrees(self):
        answer = version_2('5')
        self.assertEqual("It probably will.", answer)

    def test_snow_does_not_melt_below_three_degrees(self):
        answer = version_2('0')
        self.assertEqual("Nope! It's here to stay.", answer)

    def test_non_number_confuses_the_function(self):
        answer = version_2('lumi')
        self.assertEqual("I don't know what that means!", answer)
        
        
class TestWillTheSnowMelt3(unittest.TestCase):
    def test_snow_melts_above_three_degrees(self):
        answer = version_3('5')
        self.assertEqual("It probably will.", answer)

    def test_snow_does_not_melt_below_three_degrees(self):
        answer = version_3('0')
        self.assertEqual("Nope! It's here to stay.", answer)

    def test_non_number_confuses_the_function(self):
        answer = version_3('lumi')
        self.assertEqual("I don't know what that means!", answer)