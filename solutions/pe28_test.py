import unittest

from pe28 import solve


class Pe28Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(501), 669171001)


if __name__ == '__main__':
    unittest.main()
