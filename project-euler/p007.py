# What is the 10 001st prime number?

def nth_prime(n):
    memory = [2]
    counter = 1
    candidate = 3
    while counter < n:
        candidate_is_prime = True
        for prime in memory:
            if candidate % prime == 0:
                candidate_is_prime = False
                break
        if candidate_is_prime:
            memory.append(candidate)
            counter += 1
        candidate += 1
    return memory[-1]


number = 10001
print(nth_prime(number))
