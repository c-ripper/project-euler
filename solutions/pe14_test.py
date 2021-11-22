import unittest

from pe14 import solve


class Pe14Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(1000000), 837799)


if __name__ == '__main__':
    unittest.main()
