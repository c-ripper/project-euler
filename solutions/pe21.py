#
# Solution to Project Euler Problem #21
# Copyright (c) c-ripper. All rights reserved.
#
from utils import divisors


def is_amicable_num(n):
    dn = sum(list(divisors(n))[:-1])
    return dn != n and sum(list(divisors(dn))[:-1]) == n


def solve(n):
    return sum(filter(lambda x: is_amicable_num(x), range(2, n)))


if __name__ == '__main__':
    print(solve(10000))
