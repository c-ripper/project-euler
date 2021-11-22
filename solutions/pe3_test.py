import unittest

from pe3 import solve


class Pe3Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(600851475143), 6857)


if __name__ == '__main__':
    unittest.main()
