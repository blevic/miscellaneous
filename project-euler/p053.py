# How many, not necessarily distinct, values of "n choose k" for 1 <= n <= 100, are greater than one-million ?
from math import factorial


def n_choose_k(n, k):
    return factorial(n) // factorial(n - k) // factorial(k)


print(sum(n_choose_k(n, k) > 1000000 for n in range(1, 101) for k in range(1, n)))
