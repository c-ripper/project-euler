from math import sqrt


def divisors(n):
    yield 1
    if n == 1:
        return
    step = 2 if n % 2 == 1 else 1
    for i in range(1 + step, int(sqrt(n) + 1), step):
        if n % i == 0:
            yield i
            if i**2 == n:
                pass
            else:
                yield int(n / i)
    yield n
