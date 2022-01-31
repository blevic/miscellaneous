# Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?

max_digital_sum = 0
for a in range(1, 100):
    for b in range(1, 100):
        digital_sum = sum(int(d) for d in str(a**b))
        if digital_sum > max_digital_sum:
            max_digital_sum = digital_sum

print(max_digital_sum)
