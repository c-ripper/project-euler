import unittest

from pe19 import solve


class Pe19Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(), 171)


if __name__ == '__main__':
    unittest.main()
