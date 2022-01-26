# Find the sum of the digits in the number 100!

from math import factorial


def sum_digits(n):
    total = 0
    while n:
        total = total + n % 10
        n //= 10
    return total


print(sum_digits(factorial(100)))  # I know, this is lazy
