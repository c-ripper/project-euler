import unittest

from pe22 import solve


class Pe22Test(unittest.TestCase):

    def test_solution(self):
        self.assertEqual(solve('p022_names.txt'), 871198282)


if __name__ == '__main__':
    unittest.main()
