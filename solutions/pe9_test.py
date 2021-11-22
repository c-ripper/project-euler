import unittest

from pe9 import solve


class Pe9Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(1000), 31875000)


if __name__ == '__main__':
    unittest.main()
