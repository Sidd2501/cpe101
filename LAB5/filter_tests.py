import unittest
import filter


class TestCases(unittest.TestCase):
    def test_are_positive_1(self):
        input_list = [-1, 1, -3, 4, 5]
        self.assertListEqual(filter.are_positive(input_list), [1, 4, 5])

    def test_are_positive_2(self):
        input_list = [-1, -2, 3, -4, 5]
        self.assertListEqual(filter.are_positive(input_list), [3, 5])

    def test_are_greater_than_n_1(self):
        input_list = [0, 2, 1, 4, 3]
        n = 0
        self.assertListEqual(filter.are_greater_than_n(input_list, n), [2, 1, 4, 3])

    def test_are_greater_than_n_2(self):
        input_list = [1, 3, 9, 5]
        n = 3
        self.assertListEqual(filter.are_greater_than_n(input_list, n), [9, 5])

    def test_are_divisible_by_n_1(self):
        input_list = [2, 3, 4, 20]
        n = 2
        self.assertListEqual(filter.are_divisible_by_n(input_list, n), [2, 4, 20])

    def test_are_divisible_by_n_2(self):
        input_list = [3, 6, 9, 10, 15, 20]
        n = 2
        self.assertListEqual(filter.are_divisible_by_n(input_list, n), [6, 10, 20])


if __name__ == '__main__':
    unittest.main()
