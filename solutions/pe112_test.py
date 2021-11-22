import unittest

from pe112 import solve


class Pe112Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(0.99), 1587000)


if __name__ == '__main__':
    unittest.main()
