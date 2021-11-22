#
# Solution to Project Euler Problem #112
# Copyright (c) c-ripper. All rights reserved.
#


from itertools import count


def is_bouncy_number(n):
    dir_flag = 0
    digits = [x for x in str(n)]
    for i in range(1, len(digits)):
        if digits[i] > digits[i - 1]:
            dir_flag |= 1
        if digits[i] < digits[i - 1]:
            dir_flag |= 2
        if dir_flag == 3:
            return True
    return False


def solve(percent):
    bouncy_cnt = 0
    for x in count(1):
        if is_bouncy_number(x):
            bouncy_cnt += 1
            if bouncy_cnt / x == percent:
                break
    return x


if __name__ == '__main__':
    print(solve(0.99))
