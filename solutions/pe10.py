#
# Solution to Project Euler Problem #10
# Copyright (c) c-ripper. All rights reserved.
#


from primes import primes_list


def solve(n):
    return sum(list(primes_list(n)))


if __name__ == '__main__':
    print(solve(2000000))
