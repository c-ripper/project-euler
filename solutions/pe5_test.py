import unittest

from pe5 import solve


class Pe5Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(range(1, 21)), 232792560)


if __name__ == '__main__':
    unittest.main()
