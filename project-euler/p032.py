# Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital


def is_pandigital(p1, p2, p3):
    final_str = str(p1) + str(p2) + str(p3)
    if '0' not in final_str and len(final_str) == len(set(x for x in final_str)) == 9:
        return True
    return False


pandigital_product = []

# 1 digit * 4 digits = 4 digits
for a in range(10):
    for b in range(a, 10000):
        if is_pandigital(a, b, a*b) and a*b not in pandigital_product:
            pandigital_product.append(a*b)

# 2 digits * 3 digits = 4 digits
for a in range(100):
    for b in range(a, 1000):
        if is_pandigital(a, b, a*b) and a*b not in pandigital_product:
            pandigital_product.append(a*b)

print(sum(pandigital_product))
