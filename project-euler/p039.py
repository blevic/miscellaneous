# If p is the perimeter of a right angle triangle with integral length sides, {a,b,c},
# for which value of p ≤ 1000, is the number of solutions maximised?


def count_solutions(p):
    solutions = []
    for c1 in range(1, int(p/4) + 1):
        if p*(p-2*c1) % (2*(p-c1)) == 0:
            c2 = int(p * (p - 2 * c1)/(2 * (p - c1)))
            h = p - c1 - c2
            solution = {c1, c2, h}
            if solution not in solutions:
                solutions.append(solution)
    return len(solutions)


max_solutions = 0
max_solutions_p = 0
for perimeter in range(1000):
    sol = count_solutions(perimeter)
    if sol > max_solutions:
        max_solutions = sol
        max_solutions_p = perimeter

print(max_solutions_p)
