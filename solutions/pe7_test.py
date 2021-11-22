import unittest

from pe7 import solve


class Pe7Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(10000), 104743)


if __name__ == '__main__':
    unittest.main()
