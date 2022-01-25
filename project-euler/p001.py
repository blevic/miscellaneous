# Find the sum of all the multiples of 3 or 5 below 1000

total = 0

for e in range(1000):
    if (e % 3 == 0 or e % 5 == 0):
        total += e

print(total)
