#
# Solution to Project Euler Problem #14
# Copyright (c) c-ripper. All rights reserved.
#


def collatz_sequence(n):
    m = n
    yield m
    while m > 1:
        m = m // 2 if m % 2 == 0 else 3 * m + 1
        yield m


def solve(n):
    k = 1
    k_len = 0
    for i in range(1, n):
        l = len(list(collatz_sequence(i)))
        if l > k_len:
            k_len = l
            k = i
    return k


if __name__ == '__main__':
    print(solve(1000000))
