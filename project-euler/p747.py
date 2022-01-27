N1 = 3
N2 = 4
N3 = 6
N4 = 10

M1 = 3
M2 = 10

def phi(n):
    vide = 6*(n-2)
    nonvide = (n-1)*(n-2)/2
    return vide + nonvide

def PHI(n):
    return int(sum([phi(x) for x in range(3, n + 1)]))

print(phi(N1))
print(phi(N2))
print(phi(N3))
print(phi(N4))

print(PHI(M1))
print(PHI(M2))

print("attempts")

def r1():
    lst = []
    for i in [1,2,3]:
        for j in [1,2,3,6,12,18,24,36]:
            if [i,j] not in lst:
                lst.append([i,j])
    return lst

def r2():
    lst = []
    for i in range (-12,12+1):
        for j in [1,2,3,6,12,18,24,36]:
            if [i,j] not in lst:
                lst.append([i,j])
    return lst

def r3():
    return
    lst = []
    for i in range (-100,100):
        for j in range(1,100):
            if [i,j] not in lst:
                lst.append([i, j])
    return lst

# PHI(N) = a n^3 + bn^2 + c n + d = results

#R1 = r1()
#R2 = r2()
#R3 = r3()

R1 = [[1,6]]
R2 = [[11,2]]
R3 = r3()

guard = [1,2,3]
min_possible = 999
for a in R1:
    break
    for b in R2:
        for c in R3:
            expression1 = float(a[0]*1000000000/a[1]) + float(b[0]*1000000/b[1]) + float(c[0]*1000/c[1]) - 172166601
            expression2 = float(a[0]*1000/a[1]) + float(b[0]*100/b[1]) + float(c[0]*10/c[1]) - 345
            if (abs(expression1 - expression2) < min_possible):
                min_possible = abs(expression1 - expression2)
                guard = [a,b,c]
                print(a, b, c, min_possible)

print(guard)

def PHI_attempt(n):
    a = float(1/6)
    b = float(11/2)
    c = float(17/55)
    d = -374

    result = int(float(a*n*n*n) + float(b*n*n) + float(c*n) + float(d))

    return result

print(PHI_attempt(1000) - 172166601)
print(PHI_attempt(10) - 345)
print(PHI_attempt(100000000)%1000000007)