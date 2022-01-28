# Find the longest recurring cycle in its decimal fraction part in 1/d, with d < 1000

def longest_cycle(max_denominator):
    max_number = 0
    max_cycle_length = 0
    for denominator in range(2, max_denominator):
        remainder = 1
        for i in range(denominator):
            remainder = (remainder*10) % denominator
        base = remainder
        cycle_length = 0

        while True:
            remainder = (remainder*10) % denominator
            cycle_length += 1
            if remainder == base:
                break

        if cycle_length > max_cycle_length:
            max_number = denominator
            max_cycle_length = cycle_length

    return max_number


print(longest_cycle(1000))
