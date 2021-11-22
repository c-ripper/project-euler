#
# Solution to Project Euler Problem #4
# Copyright (c) c-ripper. All rights reserved.
#


def palindromes(n):
    for x in range(1, n):
        for y in range(1, n):
            s = x * y
            if str(s)[::-1] == str(s):
                yield s


def solve(n):
    return max(palindromes(n))


if __name__ == '__main__':
    print(solve(1000))
