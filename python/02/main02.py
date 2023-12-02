from operator import mul
from functools import reduce

"""

Advent of Code 2023
2023 December 02

Frank Schoeneman

"""

def reduce_game(line):

    def possible_set(cube, game_dict):
        num_cubes = int(cube.split(' ')[0])
        cube_color = cube.split(' ')[1]

        if game_dict[cube_color] < num_cubes: game_dict[cube_color] = num_cubes
        return 
       

    id_sets = line.split(':')
    
    game_id = id_sets[0]
    sets = id_sets[1].replace('\n', '')
  
    game_id = game_id.split(' ')[-1]
    sets = [set_.split(',') for set_ in sets.split(';')]

    game = [[set__.lstrip() for set__ in set_] for set_ in sets]

    game_dict = {key:0 for key in game_cubes.keys()}
   
    game_poss = [[ possible_set(cube, game_dict) for cube in set_] for set_ in game]
   
    return reduce(mul, game_dict.values())


def parse_input_to_games(file_path):

    with open(file_path, 'r') as f:
        all_games = f.readlines()


    return sum(list(map(reduce_game, all_games))) 




if __name__ == "__main__":

    input_file = "input.txt"

    game_cubes = {"red":12, "green":13, "blue":14}


    print ( "Total:", parse_input_to_games(input_file) )
