#
# Solution to Project Euler Problem #16
# Copyright (c) c-ripper. All rights reserved.
#


def solve(n):
    return sum(map(lambda a: int(a), list(str(n))))


if __name__ == '__main__':
    print(solve(2**1000))
