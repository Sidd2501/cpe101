# Lab 6
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

import unittest
from fold import *


class TestCases(unittest.TestCase):
    def test_sum(self):
        L1 = [1, 4, 7]
        self.assertEqual(sum(L1), 12)
        L1 = [0, -4, 8]
        self.assertEqual(sum(L1), 4)
        L1 = [1, 3, 5, 6, [7, 8]]
        self.assertEqual(sum(L1), 30)

    def test_index_of_smallest(self):
        L2 = [1, 4, -7, -1]
        self.assertEqual(index_of_smallest(L2), 2)
        L2 = [-1, 100, 4, -7, -1]
        self.assertEqual(index_of_smallest(L2), 3)
        L2 = []
        self.assertEqual(index_of_smallest(L2), -1)
        L2 = [1, 3, 5, 6, [7, 8]]
        self.assertEqual(index_of_smallest(L2), 0)


if __name__ == '__main__':
    unittest.main()
