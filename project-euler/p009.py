# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc. Find the product abc for which

for a in range(0, 333):
    for b in range(a+1, int((1000 - a)/2)):
        c = 1000 - a - b
        if a*a + b*b == c*c:
            print(a*b*c)
