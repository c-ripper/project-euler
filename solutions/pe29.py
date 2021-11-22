#
# Solution to Project Euler Problem #29
# Copyright (c) c-ripper. All rights reserved.
#


def base(n):
    for a in range(2, n + 1):
        for b in range(2, n + 1):
            yield a ** b


def solve(n):
    return len(set(base(n)))


if __name__ == '__main__':
    print(solve(100))
