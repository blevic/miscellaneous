# What is the value of the first triangle number to have over five hundred divisors?

from functools import reduce


def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


N = 1
max_factors = 0
while True:
    triang_N = N * (N + 1) / 2
    number_of_factors = len(factors(triang_N))
    if number_of_factors > max_factors:
        max_factors = number_of_factors
        if max_factors > 500:
            break
    N += 1

print(int(triang_N))
