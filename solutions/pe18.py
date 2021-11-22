#
# Solution to Project Euler Problem #18
# Copyright (c) c-ripper. All rights reserved.
#


def read_numbers(filename):
    prev_line = []
    with open(filename, 'r') as f:
        for x in [l.strip('\n').split(' ') for l in f.readlines()][::-1]:
            cur_line = list(map(lambda a: int(a), x))
            if not prev_line:
                prev_line = cur_line
            else:
                for i in range(len(cur_line)):
                    cur_line[i] += max(prev_line[i], prev_line[i + 1])
                prev_line = cur_line
    return cur_line[0]


def solve(filename):
    return read_numbers(filename)


if __name__ == '__main__':
    print(solve('pe18_numbers.txt'))
