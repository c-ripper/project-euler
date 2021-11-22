import unittest

from pe15 import solve


class Pe15Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(20), 137846528820)


if __name__ == '__main__':
    unittest.main()
