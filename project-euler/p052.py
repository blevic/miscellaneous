# Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

n = 1
while True:
    if len(set(["".join(sorted(str(i*n))) for i in range(1, 7)])) == 1:
        print(n)
        break
    n += 1
