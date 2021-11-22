#
# Solution to Project Euler Problem #7
# Copyright (c) c-ripper. All rights reserved.
#


from primes import prime_factors


# prints first n prime numbers 2,3, ....
def n_primes(n):
    p = 1
    k = 1
    while k <= n:
        if ((p == 2) or (p % 2 != 0)) and len(prime_factors(p)) == 1:
            yield p
            k += 1
        p += 1


def solve(n):
    return list(n_primes(n + 1))[-1]


if __name__ == '__main__':
    print(solve(10000))
