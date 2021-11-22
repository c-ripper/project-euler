import unittest

from pe4 import solve


class Pe4Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(1000), 906609)


if __name__ == '__main__':
    unittest.main()
