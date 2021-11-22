#
# Solution to Project Euler Problem #20
# Copyright (c) c-ripper. All rights reserved.
#

def fac(n):
    return 1 if n == 1 else n * fac(n - 1)


def solve(n):
    return sum(map(lambda x: int(x), list(str(fac(n)))))


if __name__ == '__main__':
    print(solve(100))
