import sympy

MILLION_DIGITS_OF_PI = "million.txt"


def fast_is_prime(n):
    return sympy.isprime(n)


def is_palindrome(n):
    return str(n) == str(n)[::-1]


def first_palindromic_prime(n, filename):
    if n > 3 and n % 2 == 0:
        raise Exception("N must be odd, otherwise it will be divisible by 11.")

    with open(filename, 'r') as file:
        pi = file.readline()
        for i in range(len(pi) - n):
            number = pi[i:i+n]
            if is_palindrome(number) and fast_is_prime(int(number)):
                return number

    raise Exception("No palindromic prime found. Try another file with more digits of pi.")


if __name__ == '__main__':
    answer = first_palindromic_prime(9, MILLION_DIGITS_OF_PI)
    print(answer)
