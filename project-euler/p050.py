# Which prime, below one-million, can be written as the sum of the most consecutive primes?

import sympy


def first_primes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


primes = first_primes(5000)

max_length = 0
max_prime = 0
for a in range(len(primes)):
    for b in range(a + 1, len(primes)):
        total = sum(primes[a:b])
        if sympy.isprime(total) and total < 1000000:
            length = b - a
            if length > max_length:
                max_length = length
                max_prime = total

print(max_prime)
