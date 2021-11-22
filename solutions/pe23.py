#
# Solution to Project Euler Problem #23
# Copyright (c) c-ripper. All rights reserved.
#
from utils import divisors


def is_abundant_num(n):
    return sum(list(divisors(n))[:-1]) > n


def abundant_nums(n):
    return filter(lambda x: is_abundant_num(x), range(1, n))


def is_ab_sum(n, ab_set):
    for i in range(12, n // 2 + 1):
        if i in ab_set and (n - i) in ab_set:
            return True


def solve(n):
    base_set = set(abundant_nums(n))
    return sum(list(filter(lambda x: not is_ab_sum(x, base_set), range(1, n + 1))))


if __name__ == '__main__':
    print(solve(28124))
