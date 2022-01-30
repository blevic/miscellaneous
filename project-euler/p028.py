# What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed by starting with the number 1
# in the center and moving to the right in a clockwise direction

diagonal_sum = 1
one_diagonal = 1
for layer in range(1, 1001, 2):
    for counter in range(4):
        one_diagonal += (layer + 1)
        diagonal_sum += one_diagonal

print(diagonal_sum)