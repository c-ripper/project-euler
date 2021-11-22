import unittest

from pe1 import solve


class Pe1Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(range(1000)), 233168)


if __name__ == '__main__':
    unittest.main()
