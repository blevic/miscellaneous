# Find the product of the coefficients, a and b, for the quadratic expression n^2 + a^n + b
# that produces the maximum number of primes for consecutive values of n, starting with n = 0.

import sympy


def is_prime(n):
    return sympy.isprime(n)


def prime_sequence_length(a, b):
    n = 0
    expression = b
    if not is_prime(expression):
        return 0

    while is_prime(expression):
        n += 1
        expression = n**2 + a*n + b

    return n


best_pair = (0, 0)
longest_sequence = 0
for a in range(-1000, 1001):
    for b in range(-1000, 1001):
        a_b_sequence_length = prime_sequence_length(a, b)
        if a_b_sequence_length > longest_sequence:
            best_pair = (a, b)
            longest_sequence = a_b_sequence_length

print(best_pair[0]*best_pair[1])