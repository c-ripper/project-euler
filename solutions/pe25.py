#
# Solution to Project Euler Problem #25
# Copyright (c) c-ripper. All rights reserved.
#


def solve(n):
    fb_n_2 = fb_n_1 = 1
    i = 3
    while True:
        fb_n = fb_n_2 + fb_n_1
        if len(str(fb_n)) >= n:
            return i
        fb_n_2, fb_n_1 = fb_n_1, fb_n
        i += 1


if __name__ == '__main__':
    print(solve(1000))
