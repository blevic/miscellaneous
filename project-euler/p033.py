# If the product of the two-digit digit cancelling fractions is given in its lowest common terms,
# find the value of the denominator.

def simplify(num, den):
    i = 2
    while i < min(num, den) + 1:
        if num % i == 0 and den % i == 0:
            num //= i
            den //= i
        else:
            i += 1
    return num, den


def is_digit_cancelling_two_digits(num, den):
    a = int(str(num)[0])
    b = int(str(num)[1])
    c = int(str(den)[0])
    d = int(str(den)[1])

    if b == 0 and d == 0:
        return False

    if a == c and b*den == d*num:
        return True
    if a == d and b*den == c*num:
        return True
    if b == c and a*den == d*num:
        return True
    if b == d and den == c*num:
        return True
    return False


final_num = 1
final_den = 1
for num in range(11, 100):
    for den in range(num+1, 100):
        if is_digit_cancelling_two_digits(num, den):
            final_den *= den
            final_num *= num

print(simplify(final_num, final_den)[1])
