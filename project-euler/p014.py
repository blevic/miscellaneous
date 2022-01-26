# Which starting number, under one million, produces the longest Collatz chain?

collatz_len_dict = {1: 1}


def collatz_len(n):
    if n in collatz_len_dict:
        return collatz_len_dict[n]

    next_number = int(3 * n + 1) if n % 2 else int(n / 2)
    collatz_len_dict[n] = 1 + collatz_len(next_number)

    return collatz_len_dict[n]


max_collatz_len = 0
max_collatz_number = 0

for N in range(1, 1000000):
    if N not in collatz_len_dict:
        candidate = collatz_len(N)
        if candidate > max_collatz_len:
            max_collatz_len = candidate
            max_collatz_number = N

print(max_collatz_number)
