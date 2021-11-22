import unittest

from pe20 import solve


class Pe20Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(100), 648)


if __name__ == '__main__':
    unittest.main()
