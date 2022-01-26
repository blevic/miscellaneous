# Find the sum of all the primes below two million.

from math import sqrt


def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False

    r = int(sqrt(n))
    f = 5

    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        else:
            f += 6
    return True


def sum_primes_below(n):
    if n < 2:
        return 0
    if n == 2:
        return 2
    total = 2
    for i in range(3, n, 2):
        if is_prime(i):
            total += i
    return total


print(sum_primes_below(2000000))
