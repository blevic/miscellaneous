# What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

import sympy
import math


def is_square(n):
    return math.sqrt(n).is_integer()


def first_primes_without_2(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*int((n-i*i-1)/(2*i)+1)
    return [i for i in range(3, n, 2) if sieve[i]]


PRIMES = first_primes_without_2(10000)


def is_odd_composite(n):
    return n % 2 and not sympy.isprime(n)


def conjecture_test(n):
    i = 0
    while PRIMES[i] < n:
        if is_square((n - PRIMES[i])//2):
            return True
        i += 1
    return False


n = 9
while True:
    if is_odd_composite(n):
        if not conjecture_test(n):
            break
    n += 2

print(n)
