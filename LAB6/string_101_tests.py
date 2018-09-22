# Lab 6
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

import unittest
from string_101 import *


class TestString(unittest.TestCase):
    def test_str_rot_13(self):
        str1 = 'abbeu'
        self.assertEqual(str_rot_13(str1), 'noorh')
        str2 = 'fhiruhfiurh'
        self.assertEqual(str_rot_13(str2), 'suvehusvheu')

    def test_str_translate_101(self):
        str3 = 'abcdcba'
        self.assertEqual(str_translate_101(str3, 'a', 'x'), 'xbcdcbx')
        str4 = 'abcdcba'
        self.assertEqual(str_translate_101(str4, 'b', 'x'), 'axcdcxa')


if __name__ == '__main__':
    unittest.main()
