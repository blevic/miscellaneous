# How many such Lattice paths are there through a 20×20 grid?

from math import factorial


def lattice_paths(m, n):
    return factorial(m + n) // factorial(m) // factorial(n)


print(lattice_paths(20, 20))
