import unittest
import poly


class TestPoly(unittest.TestCase):
    def assertListAlmostEqual(self, l1, l2):
        self.assertEqual(len(l1), len(l2))
        for el1, el2 in zip(l1, l2):
            self.assertAlmostEqual(el1, el2)

    def test_poly_add_1(self):
        poly1 = [2.3, 4.7, 1.0]
        poly2 = [1.2, 2.1, -3.2]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [3.5, 6.8, -2.2])

    def test_poly_add_2(self):
        poly1 = [3.2, -2, -1.2]
        poly2 = [2, 3, 2]
        poly3 = poly.poly_add2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [5.2, 1, 0.8])

    def test_poly_mult_1(self):
        poly1 = [12, 2, 4]
        poly2 = [2, 3, 21]
        poly3 = poly.poly_mult2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [24, 40, 266, 54, 84])

    def test_poly_mult_2(self):
        poly1 = [2.2, 1.5, -2.5]
        poly2 = [4.2, -6.3, 3.5]
        poly3 = poly.poly_mult2(poly1, poly2)
        self.assertListAlmostEqual(poly3, [9.24000, -7.56000, -12.249999999, 21, -8.75])


if __name__ == '__main__':
    unittest.main()
