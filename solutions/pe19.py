#
# Solution to Project Euler Problem #19
# Copyright (c) c-ripper. All rights reserved.
#

MONTH_DAYS = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def solve():
    day_of_week = 0 # Sunday
    cnt = 0
    for y in range(1900, 2001):
        for m in range(12):
            for d in range(1, MONTH_DAYS[m] + 1):
                day_of_week = (day_of_week + 1) % 7
                if d == 1 and y > 1900 and day_of_week == 0:
                    cnt += 1
            if m == 1 and (y % 400 == 0 or (y % 100 != 0 and y % 4 == 0)):
                day_of_week += 1
    return cnt


if __name__ == '__main__':
    print(solve())
