import unittest

from pe17 import solve


class Pe17Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve(1000), 21124)


if __name__ == '__main__':
    unittest.main()
