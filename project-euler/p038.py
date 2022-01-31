# What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of
# an integer with (1,2, ... , n) where n > 1?


def pandigital(n):
    concatenation = ''
    i = 1
    while True:
        product = str(i*n)
        concatenation += product

        if '0' in concatenation or len(concatenation) > 9 or len(set(list(concatenation))) != len(concatenation):
            return 0

        if len(set(list(concatenation))) == len(concatenation) == 9:
            return int(concatenation)

        i += 1


max_pandigital = 0
for i in range(10000):
    pan = pandigital(i)
    if pan > max_pandigital:
        max_pandigital = pan

print(max_pandigital)
