# Project 1
#
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

import funcs
import unittest


class TestCases(unittest.TestCase):
    def test_poundsToKG(self):
        answer1 = funcs.poundsToKG(5)
        self.assertEqual(answer1, 2.26796)
        answer2 = funcs.poundsToKG(10)
        self.assertEqual(answer2, 4.53592)

    def test_getMassObject(self):
        answer3 = funcs.getMassObject('t')
        self.assertEqual(answer3, 0.1)
        answer4 = funcs.getMassObject('p')
        self.assertEqual(answer4, 1.0)
        answer5 = funcs.getMassObject('r')
        self.assertEqual(answer5, 3.0)
        answer6 = funcs.getMassObject('l')
        self.assertEqual(answer6, 9.07)
        answer7 = funcs.getMassObject('g')
        self.assertEqual(answer7, 5.3)
        answer8 = funcs.getMassObject('a')
        self.assertEqual(answer8, 0)
        answer9 = funcs.getMassObject(10)
        self.assertEqual(answer9, 0)
        answer10 = funcs.getMassObject(-10.0)
        self.assertEqual(answer10, 0)

    def test_getVelocityObject(self):
        answer11 = funcs.getVelocityObject(3)
        self.assertAlmostEqual(answer11, 3.834057903)
        answer12 = funcs.getVelocityObject(0)
        self.assertEqual(answer12, 0)

    def test_getVelocitySkater(self):
        answer13 = funcs.getVelocitySkater(5.0, 0.1, 0)
        self.assertAlmostEqual(answer13, 0)
        answer14 = funcs.getVelocitySkater(10, 9.07, 54)
        self.assertAlmostEqual(answer14, 48.978)
