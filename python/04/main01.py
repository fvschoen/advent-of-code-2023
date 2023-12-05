"""

Advent of Code 2023
2023 December 04

Frank Schoeneman

"""


def calc_cards_points(cards):

    def proc_card(card):
        card_split = card.replace('\n', '').split(' | ')
        first_split = card_split[0]

        game_name = first_split.split(':')[0]
        win_numbers = first_split.split(':')[1]
        my_numbers = card_split[1]
  
        my_numbers = set(map(int, my_numbers.split()))
        win_numbers = set(map(int, win_numbers.split()))

        num_winning = len(my_numbers.intersection(win_numbers))
       
        if num_winning > 0: return 2**(num_winning-1)
        return 0    

    return map(proc_card, cards)


    


if __name__ == "__main__":


    with open('input.txt', 'r') as f:
        cards = f.readlines()

    print ( sum( calc_cards_points(cards) ) )
