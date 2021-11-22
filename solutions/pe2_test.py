import unittest

from pe2 import solve


class Pe2Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(4000000), 4613732)


if __name__ == '__main__':
    unittest.main()
