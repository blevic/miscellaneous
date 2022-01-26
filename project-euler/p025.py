# What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

f1 = 1
f2 = 1
n = 2

while len(str(f2)) < 1000:
    c = f2
    f2 = f1 + f2
    f1 = c
    n += 1

print(n)
