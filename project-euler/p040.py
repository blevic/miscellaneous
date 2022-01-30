# If dn represents the nth digit of the fractional part of Champernowne's constant, find the value of:
# d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

def d_n(n):
    digit_position = 0
    digit_value = -1
    i = 1
    while digit_position < n:
        insert = str(i)
        for intra_i in insert:
            digit_value = int(intra_i)
            digit_position += 1
            if digit_position == n:
                break
        i += 1
    return digit_value


product = 1
for power in range(7):
    product *= d_n(10**power)

print(product)
