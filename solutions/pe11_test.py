import unittest

from pe11 import solve


class Pe11Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve('pe11_numbers.txt'), 70600674)


if __name__ == '__main__':
    unittest.main()
