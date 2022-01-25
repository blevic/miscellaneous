# By considering the terms in the Fibonacci sequence whose values do not exceed four million,
# find the sum of the even-valued terms.

def sum_of_even_fibonacci_below(n):
    f1 = 1
    f2 = 2
    total = 0

    while f2 < n:
        if f2 % 2 == 0:
            total += f2

        next_fib = f1 + f2
        f1 = f2
        f2 = next_fib

    return total


print(sum_of_even_fibonacci_below(4000000))
