#
# Solution to Project Euler Problem #12
# Copyright (c) c-ripper. All rights reserved.
#


from itertools import count
from utils import divisors


def triangle_number(n):
    return 1 if n == 1 else n + triangle_number(n - 1)


def triangle_num_gen():
    r = 0
    for k in count(1):
        r += k
        yield r


def solve(n):
    for x in triangle_num_gen():
        if len(list(divisors(x))) > n:
            return x


if __name__ == '__main__':
    print(solve(500))
