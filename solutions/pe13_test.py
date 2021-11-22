import unittest

from pe13 import solve


class Pe13Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve('pe13_numbers.txt'), '5537376230')


if __name__ == '__main__':
    unittest.main()
