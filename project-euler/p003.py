# What is the largest prime factor of the number 600851475143 ?

def simple_factorize(n):
    while n > 1:
        for i in range(2, int(n + 1)):
            if n % i == 0:
                n /= i
                yield i
                break


factors = []
for e in simple_factorize(600851475143):
    factors.append(e)

print(factors[-1])
