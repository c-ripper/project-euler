#
# Solution to Project Euler Problem #30
# Copyright (c) c-ripper. All rights reserved.
#


def solve(power):
    acc = 0
    for i in range(10, 10 ** (power + 1)):
        if i == sum(map(lambda a: int(a) ** power, list(str(i)))):
            acc += i
    return acc


if __name__ == '__main__':
    print(solve(5))
