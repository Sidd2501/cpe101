# Project 2 - Moonlander
#
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06


import unittest
import landerFuncs


class TestCases(unittest.TestCase):
    def test_updateAcceleration(self):
        answer1 = landerFuncs.updateAcceleration(1.62, 0)
        self.assertEqual(answer1, -1.62)
        answer2 = landerFuncs.updateAcceleration(1.62, 4)
        self.assertAlmostEqual(answer2, -0.32399999)
        answer3 = landerFuncs.updateAltitude(20, 10, 3)
        self.assertEqual(answer3, 31.5)
        answer4 = landerFuncs.updateAltitude(-10, 4, -6)
        self.assertEqual(answer4, 0)
        answer5 = landerFuncs.updateAltitude(10, -4, 6)
        self.assertEqual(answer5, 9)
        answer6 = landerFuncs.updateVelocity(14, 9)
        self.assertEqual(answer6, 23)
        answer6 = landerFuncs.updateVelocity(-1, 9)
        self.assertEqual(answer6, 8)
        answer7 = landerFuncs.updateFuel(14, 0)
        self.assertEqual(answer7, 14)
        answer8 = landerFuncs.updateFuel(100, 5)
        self.assertEqual(answer8, 95)
        answer9 = landerFuncs.updateFuel(43, 9)
        self.assertEqual(answer9, 34)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
