# Find the sum of all numbers which are equal to the sum of the factorial of their digits.

from math import factorial

MAX_POSSIBLE = 7*factorial(9)  # for N > 7*factorial(9), sum_factorial_digits can never reach N


def sum_factorial_digits(n):
    total = 0
    if n < 10:
        return -1
    for d in str(n):
        total += factorial(int(d))
    return total


sum_all = 0
for n in range(MAX_POSSIBLE):
    if n == sum_factorial_digits(n):
        sum_all += n

print(sum_all)
