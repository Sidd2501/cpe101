# Lab 7
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

import unittest
from groups import *


class TestCases(unittest.TestCase):
    def test_groups_of_3(self):
        L1 = [1, 4, 7, 10, 13, 16, 19, 22, 25]
        self.assertEqual(groups_of_3(L1), [[1, 4, 7], [10, 13, 16], [19, 22, 25]])
        L1 = [1, 4, 7, 10]
        self.assertEqual(groups_of_3(L1), [[1, 4, 7], [10]])
