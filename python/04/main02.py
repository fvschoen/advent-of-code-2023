"""

Advent of Code 2023
2023 December 04

Frank Schoeneman

"""


def calc_num_matches(cards):

    def proc_card(card):
        card_split = card.replace('\n', '').split(' | ')
        first_split = card_split[0]

        game_name = first_split.split(':')[0]
        win_numbers = first_split.split(':')[1]
        my_numbers = card_split[1]
  
        my_numbers = set(map(int, my_numbers.split()))
        win_numbers = set(map(int, win_numbers.split()))

        num_winning = len(my_numbers.intersection(win_numbers))
       
        return num_winning    

    return map(proc_card, cards)


def duplicate_matches(card_wins):
  
    card_wins = {card:[card_wins[card], 1] for card in card_wins}

    for card, (wins, copies) in card_wins.items():
        
        while wins > 0:
            card_wins[card + 1][1] += copies
            wins -= 1
            card += 1        

    return sum([card_wins[card][1] for card in card_wins])


if __name__ == "__main__":


    with open('input.txt', 'r') as f:
        cards = f.readlines()

    card_match = dict( enumerate(calc_num_matches(cards)) )
    print ('total winning cards:', duplicate_matches(card_match))
