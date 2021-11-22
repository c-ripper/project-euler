#
# Solution to Project Euler Problem #6
# Copyright (c) c-ripper. All rights reserved.
#


def sum_squares(arr: []):
    return sum(map(lambda x: x**2, arr))


def squares_sum(arr: []):
    return sum(arr) ** 2


def solve(arr: []):
    return squares_sum(arr) - sum_squares(arr)


if __name__ == '__main__':
    print(solve(range(1, 101)))
