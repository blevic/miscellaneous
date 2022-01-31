# How many likely-Lychrel numbers are there below ten-thousand?

def is_palindromic(n):
    return str(n) == str(n)[::-1]


def is_likely_lychrel(n):
    iteration = 0
    number = n
    while iteration < 50:
        number += int(str(number)[::-1])
        if is_palindromic(number):
            return False  # definitely not Lychrel
        iteration += 1
    return True  # likely Lychrel


total = 0
for i in range(10000):
    if is_likely_lychrel(i):
        total += 1

print(total)
