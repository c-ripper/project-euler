import unittest

from pe30 import solve


class Pe30Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(5), 443839)


if __name__ == '__main__':
    unittest.main()
