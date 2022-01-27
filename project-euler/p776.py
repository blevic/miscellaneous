big = 1234567890123456789

def d(n):
    return sum([int(i) for i in str(n)])


def F(n):
    return


def sum_up_to(n):
    return (1+n)*n/2


N = 1234567
print (sum([x/d(x) for x in range(1, N+1)]))