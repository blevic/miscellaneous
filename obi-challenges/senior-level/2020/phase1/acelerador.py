# OBI 2020 - Senior Level - Phase 1 - Acelerador de Partículas
# https://olimpiada.ic.unicamp.br/pratique/ps/2020/f1/acelerador/

def which_door(distance):
    if distance % 8 == 6:
        return 1
    elif distance % 8 == 7:
        return 2
    elif distance % 8 == 0:
        return 3
    else:
        return -1

if __name__ == "__main__":
    distance = int(input())
    print(which_door(distance))
