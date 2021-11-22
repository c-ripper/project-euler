import unittest

from pe21 import solve


class Pe21Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(10000), 31626)


if __name__ == '__main__':
    unittest.main()
