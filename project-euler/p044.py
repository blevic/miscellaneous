# Find the pair of pentagonal numbers, Pj and Pk, for which their sum and difference are pentagonal and D = |Pk − Pj|
# is minimised; what is the value of D?

from math import sqrt


def pentagon(idx):
    return idx*(3*idx - 1)//2


def is_pentagon(n):  # idx = (1 + sqrt(1 + 24*n))/6
    sqrt_delta = sqrt(24*n + 1)
    if not sqrt_delta.is_integer():
        return False
    if (1 + sqrt_delta) % 6:
        return False
    return True


def conditions(a, b):
    p_a = pentagon(a)
    p_b = pentagon(b)

    return is_pentagon(p_a + p_b) and is_pentagon(abs(p_a - p_b))

for j in range(1, 10000):
    for k in range(1, j):
        if conditions(j, k):
            print(abs(pentagon(j) - pentagon(k)))
            break
