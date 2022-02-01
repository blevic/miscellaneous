# A number chain is created by continuously adding the square of the digits in a number to form a new number
# until it has been seen before. How many starting numbers below ten million will arrive at 89?

def sum_square_of_digits(n):
    return sum(int(d) ** 2 for d in str(n))


arrive_1 = {1}

for n in range(1, 7*9**2 + 1):
    next = n
    while next != 1 and next != 89:
        next = sum_square_of_digits(next)
    if next == 1:
        arrive_1.add(n)

print(sum(1 for n in range(1, 10**7) if sum_square_of_digits(n) not in arrive_1))
