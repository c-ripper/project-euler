import unittest

from pe8 import solve


class Pe8Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve('pe8_number.txt'), 23514624000)


if __name__ == '__main__':
    unittest.main()
