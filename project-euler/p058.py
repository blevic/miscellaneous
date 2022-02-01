# what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?

from sympy import isprime

counter_prime = 0
counter_diagonal = 1
side_length = 1
d4 = 1
while 10*counter_prime >= counter_diagonal or counter_prime == 0:
    d1 = d4 + side_length + 1
    d2 = d1 + side_length + 1
    d3 = d2 + side_length + 1
    d4 = d3 + side_length + 1

    counter_diagonal += 4
    counter_prime += sum(isprime(e) for e in [d1, d2, d3, d4])

    side_length += 2

print(side_length)
