# Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

from functools import reduce
import itertools


def find_subsets(s, n):
    return itertools.combinations(s, n)


def all_factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))


def proper_factors(n):
    factors = all_factors(n)
    factors.remove(n)
    return factors


def is_abundant(n):
    return sum(proper_factors(n)) > n


abundance = []
for i in range(1, 28123 + 1):
    if is_abundant(i):
        abundance.append(i)


remaining = set([x for x in range(28124)])

N = len(abundance)

for c1 in range(N):
    c2 = c1
    while c2 < N and abundance[c1] + abundance[c2] < 28124:
        sum_abundants = abundance[c1] + abundance[c2]
        if sum_abundants in remaining:
            remaining.remove(sum_abundants)
        c2 += 1
print(sum(remaining))
