#
# Solution to Project Euler Problem #28
# Copyright (c) c-ripper. All rights reserved.
#


def solve(n):
    s = 1
    d = 1
    for i in range(2, n+1):
        d += 2
        k1 = d**2
        k2 = k1 - d + 1
        k3 = k2 - d + 1
        k4 = k3 - d + 1
        s += k1 + k2 + k3 + k4
    return s


if __name__ == '__main__':
    print(solve(501))
