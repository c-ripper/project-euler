#
# Solution to Project Euler Problem #1
# Copyright (c) c-ripper. All rights reserved.
#


def solve(arr: []):
    return sum((x for x in arr if (x % 3 == 0) or (x % 5 == 0)))


if __name__ == '__main__':
    print(solve(range(1000)))
