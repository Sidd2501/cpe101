import unittest
import map


class TestCases(unittest.TestCase):
    def test_square_all_1(self):
        input_list = [1, 2, 3]
        self.assertListEqual(map.square_all(input_list), [1, 4, 9])

    def test_square_all_2(self):
        input_list = [-2, -1, 0, 1, 2]
        self.assertListEqual(map.square_all(input_list), [4, 1, 0, 1, 4])

    def test_add_n_all_1(self):
        input_list = [3, 2, 1, 4]
        n = 1
        self.assertListEqual(map.add_n_all(input_list, n), [4, 3, 2, 5])

    def test_add_n_all_2(self):
        input_list = [2, 3, 9, 7]
        n = -5
        self.assertListEqual(map.add_n_all(input_list, n), [-3, -2, 4, 2])

    def test_even_or_odd_all_1(self):
        input_list = [2, 3, 1, 4]
        self.assertListEqual(map.even_or_odd_all(input_list), [True, False, False, True])

    def test_even_or_odd_all_2(self):
        input_list = [0, -8, 2, 1]
        self.assertListEqual(map.even_or_odd_all(input_list), [True, True, True, False])


if __name__ == '__main__':
    unittest.main()
