#
# Solution to Project Euler Problem #13
# Copyright (c) c-ripper. All rights reserved.
#


def read_numbers(filename):
    with open(filename, 'r') as f:
        return list(map(lambda a: int(a), f.readlines()))


def solve(filename):
    return str(sum(read_numbers(filename)))[0:10]


if __name__ == '__main__':
    print(solve('pe13_numbers.txt'))
