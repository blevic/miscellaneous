# Find the first four consecutive integers to have four distinct prime factors each. What is the first of these numbers?

# yeah, it's slow, but go drink some water. it'll be finished by the time you come back


def factorize(n):
    lst = []
    while n > 1:
        for i in range(2, int(n + 1)):
            if n % i == 0:
                n /= i
                lst.append(i)
                break
    return lst


consecutive_counter = 0
n = 0
while consecutive_counter < 4:
    four_distinct_prime_factors = len(set(factorize(n))) == 4
    if four_distinct_prime_factors:
        consecutive_counter += 1
    else:
        consecutive_counter = 0
    n += 1

print(n - 4)
