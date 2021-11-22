import unittest

from pe6 import solve


class Pe6Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(range(1, 101)), 25164150)


if __name__ == '__main__':
    unittest.main()
