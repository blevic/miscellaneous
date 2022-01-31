# How many n-digit positive integers exist which are also an nth power?

def digit_count(n):
    return len(str(n))

i = 0
while True:
    if digit_count(9**i) < i:
        max_exponent = i
        break
    i += 1

counter = 0
for a in range(1, 10):
    for b in range(max_exponent):
        if digit_count(a**b) == b:
            counter += 1

print(counter)
