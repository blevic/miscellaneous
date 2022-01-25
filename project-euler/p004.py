# Find the largest palindrome made from the product of two 3-digit numbers.

from sympy.utilities.iterables import multiset_partitions

MAX_POSSIBLE = 999*999
MIN_POSSIBLE = 100*100


def is_palindrome(n):
    return str(n) == str(n)[::-1]


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


def split_two_3digit_factors(lst):
    for i in [p for p in multiset_partitions(lst, 2)]:
        f1 = product(i[0])
        f2 = product(i[1])
        if len(str(f1)) == len(str(f2)) == 3:
            print(str(f1) + "*" + str(f2) + " = "+str(f1*f2))
            return True
    return False


for number in range(MAX_POSSIBLE, MIN_POSSIBLE, -1):
    if is_palindrome(number):
        factors = simple_factorize(number)

        if split_two_3digit_factors(factors):
            break
