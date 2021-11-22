import unittest

from pe12 import solve


class Pe12Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(500), 76576500)


if __name__ == '__main__':
    unittest.main()
