#
# Solution to Project Euler Problem #2
# Copyright (c) c-ripper. All rights reserved.
#


def next_fib(n: []):
    return n[-1] + n[-2]


def fib(n):
    fib_list = [0, 1]
    while fib_list[-1] < n:
        fib_list.append(next_fib(fib_list))
    return fib_list[2:]


def solve(limit):
    return sum(x for x in fib(limit) if x % 2 == 0)


if __name__ == '__main__':
    print(solve(4000000))
