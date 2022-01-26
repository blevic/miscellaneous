# What is the sum of the digits of the number 2^1000?

def sum_digits(n):
    total = 0
    while n:
        total = total + n % 10
        n //= 10
    return total


print(sum_digits(2**1000))  # I know, this is lazy
