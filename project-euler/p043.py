# Find the sum of all 0 to 9 pandigital numbers with given property.

from itertools import permutations


def given_property(n):
    if int(n[1:4]) % 2:
        return False
    if int(n[2:5]) % 3:
        return False
    if int(n[3:6]) % 5:
        return False
    if int(n[4:7]) % 7:
        return False
    if int(n[5:8]) % 11:
        return False
    if int(n[6:9]) % 13:
        return False
    if int(n[7:10]) % 17:
        return False
    return True


if __name__ == "__main__":
    print(sum(int("".join(n)) for n in permutations(str(x) for x in range(10)) if given_property("".join(n))))
