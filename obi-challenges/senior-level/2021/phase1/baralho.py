# OBI 2021 - Senior Level - Phase 1 - Baralho
# https://olimpiada.ic.unicamp.br/pratique/ps/2021/f1/baralho/

# Input:  Sequence of characters (at least 3, up to 156) representing cards: 3 characters for each card
#         Each card has the format ddN, where dd is the rank (from 01 to 13) and N is the suit (C, E, U, P)

# Output: 4 rows representing the number of missing cards in each rank (in order: C, E, U, P)
#         if a rank has duplicate cards, print "erro" instead of the number of cards


# Example:
# Input                                     --> Output
#                                         |     4
# 01C02C03C04C05C07C09C10C11C02E02E03E11U | --> erro
#                                         |     12
#                                         |     13

if __name__ == '__main__':
    all_cards = input()
    all_cards_split = [all_cards[i:i + 3] for i in range(0, len(all_cards), 3)]

    cards_dict = {
        'C': [],
        'E': [],
        'U': [],
        'P': []
        }

    for card in all_cards_split:
        cards_dict[card[2]].append(int(card[0:2]))

    for rank in ['C', 'E', 'U', 'P']:
        if len(set(cards_dict[rank])) == len(cards_dict[rank]):
            print(13 - len(cards_dict[rank]))
        else:
            print("erro")