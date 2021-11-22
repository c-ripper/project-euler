import unittest

from pe25 import solve


class Pe25Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(1000), 4782)


if __name__ == '__main__':
    unittest.main()
