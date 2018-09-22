# Lab 3
#
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

import unittest
import conditional


class TestCases(unittest.TestCase):
    def test_max_101(self):
        answer1 = conditional.max_101(5, 20)
        self.assertEqual(answer1, 20)
        answer2 = conditional.max_101(-10, 0)
        self.assertEqual(answer2, 0)
        answer3 = conditional.max_101(99.2, 99.3)
        self.assertEqual(answer3, 99.3)

    def test_max_of_three(self):
        answer4 = conditional.max_of_three(-10, 0, 10)
        self.assertEqual(answer4, 10)
        answer5 = conditional.max_of_three(9.7, 9.8, 9.9)
        self.assertEqual(answer5, 9.9)
        answer6 = conditional.max_of_three(4, 20, 70)
        self.assertEqual(answer6, 70)

    def test_rental_late_fee(self):
        answer7 = conditional.rental_late_fee(0)
        self.assertEqual(answer7, 0)
        answer8 = conditional.rental_late_fee(-10)
        self.assertEqual(answer8, 0)
        answer9 = conditional.rental_late_fee(25)
        self.assertEqual(answer9, 100)
        answer10 = conditional.rental_late_fee(14)
        self.assertEqual(answer10, 7)
        answer11 = conditional.rental_late_fee(5)
        self.assertEqual(answer11, 5)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
