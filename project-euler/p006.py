# Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares(n):
    return n*(n + 1)*(2*n + 1)/6


def square_of_sum(n):
    return ((1 + n)*n/2)*(1 + n)*n/2


number = 100
diff = square_of_sum(number) - sum_of_squares(number)
print(int(diff))
