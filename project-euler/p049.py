# The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways:
# (i) each of the three terms are prime, and, (ii) each of the 4-digit numbers are permutations of one another.
#
# There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property,
# but there is one other 4-digit increasing sequence.
#
# What 12-digit number do you form by concatenating the three terms in this sequence?

import itertools


def first_primes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


primes = [x for x in first_primes(10000) if x > 999]

categories = {}

for prime in primes:
    category = "".join(sorted(str(prime)))
    if category in categories:
        categories[category].append(prime)
    else:
        categories[category] = [prime]

for cat in categories:
    if len(categories[cat]) > 2:
        for triad in itertools.combinations(categories[cat], 3):
            if (triad[0] + triad[2])//2 == triad[1]:
                print("".join(str(x) for x in list(triad)))