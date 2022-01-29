# Find the last ten digits of the series, 1^ 1 + 2^2 + 3^3 + ... + 1000^1000.

print(sum(x**x for x in range(1001)) % 10**10)
