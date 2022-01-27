# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

import itertools
import sympy

MAX_PRIME_GUESS = 10000


def find_subsets(s, n):
    return itertools.combinations(s, n)


def first_primes(n):
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i]:
            sieve[i*i::2*i] = [False]*int((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3, n, 2) if sieve[i]]


def fast_is_prime(n):
    return sympy.isprime(n)


def slow_is_prime(n):
    if n == 2 or n == 3:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    elif n < 9:
        return True
    elif n % 3 == 0:
        return False

    r = int(n**0.5)
    f = 5

    while f <= r:
        if n % f == 0 or n % (f + 2) == 0:
            return False
        else:
            f += 6
    return True


def is_prime(n):
    return fast_is_prime(n)


def check(lst):
    for e in find_subsets(lst, 2):
        s0 = str(e[0])
        s1 = str(e[1])
        i0 = int(s0 + s1)
        i1 = int(s1 + s0)
        if not is_prime(i0) or not is_prime(i1):
            return False
    return True


def find_pairs(lst):
    pairs = set()
    for p in find_subsets(lst, 2):
        if check(p):
            pairs.add(p)
    return pairs


def create_dict(lst):
    pairs_dict = {}
    for e in lst:
        a = e[0]
        b = e[1]

        if a not in pairs_dict:
            pairs_dict[a] = [b]
        else:
            if b not in pairs_dict[a]:
                pairs_dict[a].append(b)
        if b not in pairs_dict:
            pairs_dict[b] = []
    return pairs_dict


def intersect(a, b):
    return list(set(a) & set(b))


def iterate_intersections(dict):
    result = []
    for p1 in dict:
        for p2 in dict[p1]:
            i1 = intersect(dict[p1], dict[p2])
            for p3 in i1:
                i2 = intersect(i1, dict[p3])
                for p4 in i2:
                    i3 = intersect(i2, dict[p4])
                    for p5 in i3:
                        result.append([p1, p2, p3, p4, p5])
    return result


if __name__ == '__main__':
    primes_array = first_primes(MAX_PRIME_GUESS)

    l1 = [x for x in primes_array if x % 3 != 1]
    l2 = [x for x in primes_array if x % 3 != 2]

    p1 = find_pairs(l1)
    p2 = find_pairs(l2)

    d1 = create_dict(p1)
    d2 = create_dict(p2)

    c1 = iterate_intersections(d1)
    c2 = iterate_intersections(d2)

    candidates = c1 + c2

    lowest_sum = min([sum(x) for x in candidates]) if candidates else 0
    print(lowest_sum)
