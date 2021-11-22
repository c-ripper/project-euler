import unittest

from pe10 import solve


class Pe10Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(2000000), 142913828922)


if __name__ == '__main__':
    unittest.main()
