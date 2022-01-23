# OBI 2014 - Senior Level - Phase 1 - Carteiro
# https://olimpiada.ic.unicamp.br/pratique/pu/2014/f1/carteiro/

# Input:  2 integers: N and M
#         houses -> N distinct integers, in ascending order (1 <= N <= 45000), identifying house numbers
#         journey -> M distinct integers, indicating an ordered journey from house to house (1 <= M <= 45000)
#         every element of 'journey' is within 'houses', and the distance between two consecutive houses is 1

# Output: total journey length, starting from the 1st house and visiting all houses listed in journey, in that order

# Example:
# Input          -> Output
# 5 5           |
# 1 5 10 20 40  |--> 10
# 10 20 10 40 1 |

if __name__ == '__main__':
    N, M = [int(i) for i in input().split()]
    houses = input().split()  # N houses
    journey = input().split()  # M visits

    # adds initial position
    journey.insert(0, houses[0])

    pos_dict = {}
    for idx, house in enumerate(houses):
        pos_dict[house] = idx

    total_distance = 0
    for idx in range(M):
        total_distance += abs(pos_dict[journey[idx+1]] - pos_dict[journey[idx]])  # journey

    print(total_distance)
