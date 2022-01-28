# Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

MAX_POSSIBLE = 6*9**5

print(sum(i for i in range(10, MAX_POSSIBLE) if int(sum(int(x)**5 for x in str(i))) == i))
