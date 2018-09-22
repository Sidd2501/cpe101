# Lab 3
#
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

import unittest
import logic


class TestCases(unittest.TestCase):
    def test_is_even(self):
        answer0 = logic.is_even(5)
        self.assertEqual(answer0, 0)
        answer1 = logic.is_even(8)
        self.assertEqual(answer1, 1)
        answer2 = logic.is_even(0)
        self.assertEqual(answer2, 1)

    def test_in_an_interval(self):
        answer3 = logic.in_an_interval(-10)
        self.assertEqual(answer3, 0)
        answer4 = logic.in_an_interval(0)
        self.assertEqual(answer4, 1)
        answer5 = logic.in_an_interval(9)
        self.assertEqual(answer5, 0)
        answer6 = logic.in_an_interval(20)
        self.assertEqual(answer6, 1)
        answer7 = logic.in_an_interval(122)
        self.assertEqual(answer7, 1)
        answer8 = logic.in_an_interval(127)
        self.assertEqual(answer8, 1)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
