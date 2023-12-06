from functools import reduce
from operator import mul

def part_01(race):
   
    time, dist = race

    return sum([(time - t_h) * t_h > dist for t_h in range(time)])


if __name__ == "__main__":


    with open('input.txt') as f:
        lines = f.readlines()

    times = list(map(int, lines[0].split(':')[1].split()))
    dists = list(map(int, lines[1].split(':')[1].split()))

    races = list(zip(times, dists))

    print ( "Total ways to win:",  reduce(mul,  map(part_01, races)) )
