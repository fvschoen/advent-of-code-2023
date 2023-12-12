
import itertools

def read_space_img(lines):

    return [list(line.strip()) for line in lines]

def expansion(space):

    def space_expand_row(img):
        for row in img:
            yield row
            if not '#' in row: 
                yield row

    space = list(space_expand_row(space))
    
    # transpose to expand columns
    space = list(map(list, zip(*space)))

    space = list(space_expand_row(space))
    
    # transpose to return original
    space = list(map(list, zip(*space)))

    galaxy_loc = {}

    galaxy_idx = 1 
    for i in range(len(space)):
        for j in range(len(space[0])):
            if space[i][j] == '#': 
                space[i][j] = galaxy_idx
                galaxy_loc[galaxy_idx] = (i, j)
                galaxy_idx += 1
   
    return space, galaxy_loc

def calc_dist_pairs_galaxies(galaxy_loc):

    total_dists = 0
    for galaxy_1, galaxy_2 in itertools.combinations(galaxy_loc.keys(), r=2):

        i1, j1 = galaxy_loc[galaxy_1]
        i2, j2 = galaxy_loc[galaxy_2]

        dist = abs(i1 - i2) + abs(j1 - j2) 
        total_dists += dist        
 
    return total_dists

if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        lines = f.readlines()


    space = read_space_img(lines)

    space, galaxy_loc = expansion(space)

    print ("Sum of distances between pairs of galaxies:", calc_dist_pairs_galaxies(galaxy_loc))

    
