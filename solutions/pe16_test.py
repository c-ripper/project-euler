import unittest

from pe16 import solve


class Pe16Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(2**1000), 1366)


if __name__ == '__main__':
    unittest.main()
