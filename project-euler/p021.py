# Evaluate the sum of all the amicable numbers under 10000

from functools import reduce


def all_factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def proper_factors(n):
    factors = all_factors(n)
    factors.remove(n)
    return factors


def sum_amicable(n):
    total = 0
    for i in range(2, n + 1):
        j = sum(proper_factors(i))
        if j < i == sum(proper_factors(j)):
            total += i + j
    return total


print(sum_amicable(10000))
