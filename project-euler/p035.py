# How many circular primes are there below one million?

from sympy import isprime


def is_circular_prime(n):
    for i in range(len(str(n))):
        p1 = str(n)[:i]
        p2 = str(n)[i:]
        rotation = int(str(p2) + str(p1))
        if not isprime(rotation):
            return False
    return True

print(sum(1 for x in range(1000000) if is_circular_prime(x)))