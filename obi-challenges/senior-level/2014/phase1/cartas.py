# OBI 2014 - Senior Level - Phase 1 - Cartas
# https://olimpiada.ic.unicamp.br/pratique/pu/2014/f1/cartas/

# Input:  sequence of 5 distinct integers, ranged 1 to 13
# Output: 'C' if sorted in ascending order
#         'D' if sorted in descending order
#         'N' otherwise

# Examples:
# Input       -> Output
# 1 2 3 5 6   -> C
# 5 7 10 9 11 -> N
# 12 10 4 3 2 -> D

def is_it_sorted(l):
    # small list, we may sort it
    if sorted(l) == l:
        return 'C'
    elif sorted(l) == l[::-1]:
        return 'D'
    else:
        return 'N'

if __name__ == '__main__':
    list_integers = [int(i) for i in input().split()]
    print(is_it_sorted(list_integers))