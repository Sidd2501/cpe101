#Lab 2 Test Cases
#Name: Sid Sharma
#Section: 06

import unittest
import funcs
from math import *

class TestCases(unittest.TestCase):
   def test_math_func1(self):
      x=1
      y=1
      answer1 = funcs.math_func1(x,y)
      self.assertAlmostEqual(answer1, 0.16666666666666)
      x=2
      y=2
      answer2 = funcs.math_func1(x,y)
      self.assertAlmostEqual(answer2, 0.94117647)

   def test_math_func2(self):
      a=1
      b=4
      c=0
      answer3 = funcs.math_func2(a, b, c)
      self.assertEqual(answer3, 0)
      a=2
      b=6
      c=3
      answer4 = funcs.math_func2(a, b, c)
      self.assertAlmostEqual(answer4, -0.63397459621)

   def test_d(self):
      x1 = 1
      y1 = 2
      x2 = 2
      y2 = 3
      answer5 = funcs.d(x1, y1, x2, y2)
      self.assertAlmostEqual(answer5, 1.41421356237)
      x1 = 2
      y1 = 3
      x2 = 4
      y2 = 9
      answer6 = funcs.d(x1, y1, x2, y2)
      self.assertAlmostEqual(answer6, 6.324555320336) 
      
   def test_is_negative(self):
      inp1 = int(-3)
      self.assertTrue(funcs.is_negative(-3))
      inp2 = int(5) 
      self.assertFalse(funcs.is_negative(5))

   def test_dividable_by_5(self):
      inp3 = int(40) % 5
      self.assertFalse(funcs.dividable_by_5(40))
      inp4 = int(43) % 5
      self.assertTrue(funcs.dividable_by_5(43))

# Run the unit tests.
if __name__ == '__main__':
   unittest.main()
