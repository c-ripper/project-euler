import unittest

from pe24 import solve


class Pe24Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(1000000), 2783915460)


if __name__ == '__main__':
    unittest.main()
