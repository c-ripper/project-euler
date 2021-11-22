#
# Solution to Project Euler Problem #17
# Copyright (c) c-ripper. All rights reserved.
#


WORDS = {
    1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight",
    9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen",
    16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty",
    40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"
}


def spell_number(n):
    if n in WORDS:
        return WORDS[n]
    if n in range(21, 100) and n % 10 != 0:
        return "{} {}".format(WORDS[n - (n % 10)], WORDS[n % 10])
    if n // 1000 > 0:
        if n % 1000 == 0:
            return "{} thousand".format(WORDS[n // 1000])
        else:
            return "{} thousand and {}".format(WORDS[n // 1000], spell_number(n % 1000))
    if n // 100 > 0:
        if n % 100 == 0:
            return "{} hundred".format(WORDS[n // 100])
        else:
            return "{} hundred and {}".format(WORDS[n // 100], spell_number(n % 100))


def solve(n):
    return sum(map(lambda x: len(spell_number(x).replace(' ', '')), range(1, n + 1)))


if __name__ == '__main__':
    print(solve(1000))
