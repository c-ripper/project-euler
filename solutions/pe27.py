#
# Solution to Project Euler Problem #27
# Copyright (c) c-ripper. All rights reserved.
#
from primes import prime_factors, PRIMES_1000


def f(n, a, b):
    return n**2 + a*n + b


def is_prime(p):
    if p < 2:
        return False
    else:
        return len(prime_factors(p)) == 1


def solve():
    max_n = max_a = max_b = 0
    # b should always be a prime
    for b in PRIMES_1000:
        for a in range(-999, 1000):
            n = 1
            while True:
                if is_prime(f(n, a, b)):
                    if n > max_n:
                        max_a = a
                        max_b = b
                        max_n = n
                    n += 1
                else:
                    break
    return max_a * max_b


if __name__ == '__main__':
    print(solve())
