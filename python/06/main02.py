from functools import reduce
from operator import mul

def part_02(race):
   
    time, dist = race

    return sum([(time - t_h) * t_h > dist for t_h in range(time)])


if __name__ == "__main__":


    with open('input.txt') as f:
        lines = f.readlines()

    time = int("".join(lines[0].split(':')[1].strip().split()))
    dist = int("".join(lines[1].split(':')[1].strip().split()))

    race = (time, dist)
    print ( "Total ways to win:",  part_02(race))
