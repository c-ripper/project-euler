#
# Solution to Project Euler Problem #24
# Copyright (c) c-ripper. All rights reserved.
#


from itertools import permutations


def solve(n):
    return int(''.join(map(lambda y: str(y), [x for x in permutations([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])][n - 1])))


if __name__ == '__main__':
    print(solve(1000000))
