# What is the largest n-digit pandigital (makes use of all the digits 1 to n exactly once) prime that exists?

import itertools
import sympy

digits = list(range(7, 0, -1))  # no need to check 9 and 8 digits (they are multiples of 3)

count = 0
for permutation in itertools.permutations(digits):
    number = int("".join(str(x) for x in permutation))
    if sympy.isprime(number):
        print(number)
        break
