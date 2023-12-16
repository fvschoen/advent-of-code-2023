
def parse_rocks(lines):

    return [list(line.strip()) for line in lines]

def roll_rocks(rocks):

    rocks = [''.join(line) for line in rocks]

    for _ in range(len(rocks)):
        rocks = map(lambda line : line.replace('.O', 'O.'), rocks)

    rocks = [list(line) for line in rocks]

    return rocks

def calc_load(rocks):

    return sum([(w+1)*(line.count('O')) for w, line in enumerate(rocks[::-1])])

if __name__ == '__main__':


    with open('input.txt', 'r') as f:
        lines = f.readlines()

    rocks = parse_rocks(lines)

    # transpose for more efficient rolling 
    rocks = list(map(list, zip(*rocks)))

    rocks = roll_rocks(rocks)

    rocks = list(map(list, zip(*rocks)))

    print ('Total load:', calc_load(rocks))

