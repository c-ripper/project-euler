#
# Solution to Project Euler Problem #11
# Copyright (c) c-ripper. All rights reserved.
#


import operator
from functools import reduce


def file2matrix(filename):
    with open(filename, 'r') as f:
        m = []
        for x in [l.strip('\n').split(' ') for l in f.readlines()]:
            m.append(list(map(lambda a: int(a), x)))
        return m


def horizontal_combinations(m):
    for row in range(0, len(m)):
        for i in range(0, len(m) - 3):
            yield m[row][i:i + 4]


def vertical_combinations(m):
    for col in range(0, len(m)):
        for i in range(0, len(m) - 3):
            yield m[i][col], m[i + 1][col], m[i + 2][col], m[i + 3][col]


# Diagonal: top left to bottom right
def diagonal1_combinations(m):
    for i in range(0, len(m) - 3):
        for j in range(0, len(m) - 3):
            yield m[i][j], m[i + 1][j + 1], m[i + 2][j + 2], m[i + 3][j + 3]


# Diagonal: top right to bottom left
def diagonal2_combinations(m):
    for i in range(0, len(m) - 3):
        for j in reversed(range(3, len(m) - 1)):
            yield m[i][j], m[i + 1][j - 1], m[i + 2][j - 2], m[i + 3][j - 3]


def greatest_product(arr):
    return max(list(map(lambda a: reduce(operator.mul, a, 1), arr)))


def solve(filename):
    matrix = file2matrix(filename)
    hor_max_product = greatest_product(list(horizontal_combinations(matrix)))
    vert_max_product = greatest_product(list(vertical_combinations(matrix)))
    diag1_max_product = greatest_product(list(diagonal1_combinations(matrix)))
    diag2_max_product = greatest_product(list(diagonal2_combinations(matrix)))
    return max(hor_max_product, vert_max_product, diag1_max_product, diag2_max_product)


if __name__ == '__main__':
    print(solve('pe11_numbers.txt'))
