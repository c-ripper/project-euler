#
# Solution to Project Euler Problem #5
# Copyright (c) c-ripper. All rights reserved.
#


from functools import reduce
from collections import Counter
from primes import prime_factors


def factors(arr: []):
    factors_out = dict()
    for x in arr[::-1]:
        factors_counters = Counter(prime_factors(x))
        for y in factors_counters.keys():
            if y not in factors_out.keys():
                factors_out[y] = factors_counters[y]
            else:
                if factors_out[y] < factors_counters[y]:
                    factors_out[y] = factors_counters[y]
    return factors_out


def solve(arr: []):
    factor_base = factors(list(arr))
    return reduce(lambda x, y: x * y, list(map(lambda it: it[0] ** it[1], list(factor_base.items()))))


if __name__ == '__main__':
    print(solve(range(1, 21)))
