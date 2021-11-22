import unittest

from pe26 import solve


class Pe26Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(), 983)


if __name__ == '__main__':
    unittest.main()
