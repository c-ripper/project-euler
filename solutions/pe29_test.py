import unittest

from pe29 import solve


class Pe29Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(100), 9183)


if __name__ == '__main__':
    unittest.main()
