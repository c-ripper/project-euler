import unittest

from pe18 import solve


class Pe18Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve('pe18_numbers.txt'), 1074)


if __name__ == '__main__':
    unittest.main()
