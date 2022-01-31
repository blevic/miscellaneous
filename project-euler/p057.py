# In the first one-thousand expansions of sqrt(2), how many fractions contain a num with more digits than the den?

iteration = 0
fraction = (1, 1)
counter = 0
while iteration < 1000:
    fraction = (2*fraction[1] + fraction[0], fraction[0] + fraction[1])
    iteration += 1
    if len(str(fraction[0])) != len(str(fraction[1])):
        counter += 1

print(counter)
