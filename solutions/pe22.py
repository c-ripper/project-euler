#
# Solution to Project Euler Problem #22
# Copyright (c) c-ripper. All rights reserved.
#


def calc_score(name, index):
    return sum(map(lambda x: (ord(x) - 0x40), [c for c in name])) * index


def read_names(filename):
    with open(filename, 'r') as f:
        return [(i, name) for i, name in enumerate(sorted([x.strip('"') for x in f.read().split(',')]))]


def solve(filename):
    return sum(map(lambda it: calc_score(it[1], it[0] + 1), read_names(filename)))


if __name__ == '__main__':
    print(solve('p022_names.txt'))
