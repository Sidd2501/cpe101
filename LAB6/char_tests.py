# Lab 6
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

import unittest
from char import *


class TestChar(unittest.TestCase):
    def test_is_lower_101(self):
        str1 = 'A'
        self.assertEqual(is_lower_101(str1), False)
        str2 = 'b'
        self.assertEqual(is_lower_101(str2), True)

    def test_rot_13(self):
        str3 = 'a'
        self.assertEqual(char_rot13(str3), 'n')
        str4 = 'A'
        self.assertEqual(char_rot13(str4), 'N')


if __name__ == '__main__':
    unittest.main()
