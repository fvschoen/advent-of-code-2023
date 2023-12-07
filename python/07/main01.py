from collections import Counter

def parse_hands(lines):

    def parse_line(line):

        hand, bid = line.split(' ')[0], line.split(' ')[1].strip()
        hand_counts = Counter(hand.strip())

        return {'hand':hand, 'bid':bid, 'counts':hand_counts}


    return list(map(parse_line, lines))


def calc_winnings(rank_bid):

    return rank_bid[0] * rank_bid[1]

if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        lines = f.readlines()

    cards = 'AKQJT98765432'
    card_val = {card:val for val, card in enumerate(cards[::-1])}    

    hands = parse_hands(lines)

    sorted_hands = sorted(hands, 
                   key=lambda x : (sorted(x['counts'].values(), reverse=True), 
                                   [card_val[card] for card in x['hand']]),
                   reverse=True)


    print ( "Total Winnings:", sum([ (len(hands) - i) * int(hand['bid']) 
                               for i, hand in enumerate(sorted_hands) ]) ) 
    
