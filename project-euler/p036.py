# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

def is_palindromic_base_10(n):
    return str(n) == str(n)[::-1]


def is_palindromic_base_2(n):
    return bin(n)[2:] == bin(n)[2:][::-1]


print(sum(x for x in range(1000000+1) if is_palindromic_base_2(x) and is_palindromic_base_10(x)))
