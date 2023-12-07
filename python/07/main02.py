from collections import Counter
from itertools import product

def parse_hands(lines):

    def parse_line(line):

        hand, bid = line.split(' ')[0], line.split(' ')[1].strip()
        hand_counts = Counter(hand.strip())

        return {'hand':hand, 'bid':bid, 'counts':hand_counts}


    return list(map(parse_line, lines))


def score_jokers(hand):


    def gen_wild_hands(jhand):
        
        cards = 'AKQT98765432'
        j_idx = [idx for idx, card in enumerate(jhand) if card == 'J']

        new_hands_sub = product(cards, repeat=len(j_idx))

        new_hands = []
        for sub in new_hands_sub:
            new_hand = list(jhand)
            for idx, card in zip(j_idx, sub):
                new_hand[idx] = card
            new_hands.append(''.join(new_hand))

        return new_hands
    

    # if no J, return hand but with score 
   
    if not 'J' in hand['hand']:
        hand_counter = Counter(hand['hand'])
        hand['score'] = hand_counter.values()

    # if J(s) present, do the following:
    # expand all Js 
    # score each hand
    # take max scored hand
    # return original hand (with J present) with max score

    else:
        poss_hands = gen_wild_hands(hand['hand'])
        poss_scores = sorted([sorted(Counter(x).values(), reverse=True) for x in poss_hands], 
                             reverse=True)
        hand['score'] = poss_scores[0]

    return hand


def calc_winnings(rank_bid):

    return rank_bid[0] * rank_bid[1]

if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        lines = f.readlines()

    cards = 'AKQT98765432J' # J Joker now weakest individual
    card_val = {card:val for val, card in enumerate(cards[::-1])}    

    hands = parse_hands(lines)

    scored_hands = list(map(score_jokers, hands))

    sorted_hands = sorted(scored_hands, 
                   key=lambda x : (sorted(x['score'], reverse=True), 
                                   [card_val[card] for card in x['hand']]),
                   reverse=True)


    print ( "Total Winnings:", sum([ (len(hands) - i) * int(hand['bid']) 
                               for i, hand in enumerate(sorted_hands) ]) ) 
    
