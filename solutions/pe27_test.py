import unittest

from pe27 import solve


class Pe27Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(), -59231)


if __name__ == '__main__':
    unittest.main()
