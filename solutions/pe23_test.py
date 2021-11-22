import unittest

from pe23 import solve


class Pe23Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(28124), 4179871)


if __name__ == '__main__':
    unittest.main()
