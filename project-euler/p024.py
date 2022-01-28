# What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import itertools

letters = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

count = 0
for e in itertools.permutations(letters):
    count += 1
    if count == 1000000:
        print("".join(str(x) for x in e))
        break