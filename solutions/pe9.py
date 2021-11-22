#
# Solution to Project Euler Problem #9
# Copyright (c) c-ripper. All rights reserved.
#


from functools import reduce


def pythagorean_triplets(n):
    for x in range(1, n + 1):
        for y in range(x + 1, n - x):
            z = n - x - y
            if x != y != z:
                m = max(x, y, z)
                if m**2 == sum(list(map(lambda a: a**2, list(filter(lambda b: b != m, [x, y, z]))))):
                    return [x, y, z]


def solve(n):
    return reduce(lambda x, y: x * y, pythagorean_triplets(n))


if __name__ == '__main__':
    print(solve(1000))
