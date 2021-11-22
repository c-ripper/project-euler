#
# Solution to Project Euler Problem #3
# Copyright (c) c-ripper. All rights reserved.
#


from primes import prime_factors


def solve(n):
    return prime_factors(n)[-1]


if __name__ == '__main__':
    print(solve(600851475143))
