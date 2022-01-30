# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

from sympy import isprime


def is_truncatable_prime(n):
    if not isprime(n):
        return False
    for i in range(1, len(str(n))):
        p1 = int(str(n)[:i])
        p2 = int(str(n)[i:])
        if not isprime(p1) or not isprime(p2):
            return False
    return True


count = 0
sum_truncatables = 0
i = 11
while count < 11:
    if is_truncatable_prime(i):
        sum_truncatables += i
        count += 1
    i += 2

print(sum_truncatables)
