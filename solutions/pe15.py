#
# Solution to Project Euler Problem #15
# Copyright (c) c-ripper. All rights reserved.
#
# Use dynamic programming
import numpy as np


def paths(i, j, arr):
    if i == 0 and j == 0:
        return 0
    if i == 0 or j == 0:
        return 1

    if arr[i - 1][j] == 0:
        arr[i - 1][j] = paths(i - 1, j, arr)
    if arr[i][j - 1] == 0:
        arr[i][j - 1] = paths(i, j - 1, arr)

    return arr[i - 1][j] + arr[i][j - 1]


def solve(n):
    calculated_paths = np.zeros((n + 1, n + 1), dtype=int)
    for i in range(1, n + 1):
        calculated_paths[0][i] = calculated_paths[i][0] = 1
    return paths(n, n, calculated_paths)


if __name__ == '__main__':
    print(solve(20))
