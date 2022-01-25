# What is the 10 001st prime number?
from math import sqrt


def very_slow_and_awful_nth_prime(n):
    memory = [2]
    counter = 1
    candidate = 3
    while counter < n:
        candidate_is_prime = True
        for prime in memory:
            if candidate % prime == 0:
                candidate_is_prime = False
                break
        if candidate_is_prime:
            memory.append(candidate)
            counter += 1
        candidate += 2
    return memory[-1]


def is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False

    r = int(sqrt(n))
    f = 5

    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        else:
            f += 6
    return True


def fast_nth_prime(n):
    count = 1
    candidate = 1
    while count < n:
        candidate += 2
        if is_prime(candidate):
            count += 1
    return candidate


number = 10001
print(fast_nth_prime(number))
