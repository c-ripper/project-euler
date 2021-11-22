#
# Solution to Project Euler Problem #8
# Copyright (c) c-ripper. All rights reserved.
#


from functools import reduce


def file2str(filename):
    with open(filename, 'r') as f:
        return "".join([l.strip('\n') for l in f.readlines()])


def adj13_products(s):
    for k in range(0, len(s) - 12, 1):
        yield reduce(lambda x, y: x * y, [int(x) for x in s[k:k+13]])


def solve(filename):
    return max(adj13_products(file2str(filename)))


if __name__ == '__main__':
    print(solve('pe8_number.txt'))
