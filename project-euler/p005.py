# What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

def simple_factorize(n):
    lst = []
    while n > 1:
        for i in range(2, int(n + 1)):
            if n % i == 0:
                n /= i
                lst.append(i)
                break
    return lst


def product(lst):
    f = 1
    for i in lst:
        f *= i
    return f


list_all_factors = []

for number in range(1, 20+1):
    factors = simple_factorize(number)

    for candidate in list_all_factors:
        if candidate in factors:
            factors.remove(candidate)

    list_all_factors += factors

print(product(list_all_factors))
