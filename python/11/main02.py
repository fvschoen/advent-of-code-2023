
import itertools

def read_space_img(lines):

    return [list(line.strip()) for line in lines]

def expansion(space, expand=True):

    def space_expand_row(img):
        for idx, row in enumerate(img):
            if not '#' in row: 
                yield idx

    row_exp, col_exp = None, None

    if expand: row_exp = list(space_expand_row(space))
    
    # transpose to expand columns
    space = list(map(list, zip(*space)))

    if expand: col_exp = list(space_expand_row(space))
    
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
   
    return galaxy_loc, row_exp, col_exp

def calc_dist_pairs_galaxies(galaxy_loc):

    dist_map = {}
    total_dists = 0
    for galaxy_1, galaxy_2 in itertools.combinations(galaxy_loc.keys(), r=2):

        i1, j1 = galaxy_loc[galaxy_1]
        i2, j2 = galaxy_loc[galaxy_2]

        dist = abs(i1 - i2) + abs(j1 - j2) 
        dist_map[(galaxy_1, galaxy_2)] = dist
        total_dists += dist        
 
    return dist_map


def diff_galaxy_dists(dist_map, galaxy_loc, row_exp, col_exp, exp_rate=2.):

    total_dists = 0.
    for k in dist_map:
        k1, k2 = k
        i1, j1 = galaxy_loc[k1]
        i2, j2 = galaxy_loc[k2]

        imin, imax = min(i1, i2), max(i1, i2)
        jmin, jmax = min(j1, j2), max(j1, j2)

        row_exp_int = [imin < i < imax for i in row_exp]#)
        col_exp_int = [jmin < j < jmax for j in col_exp]#)

        n_row_exp_int = sum(row_exp_int)
        n_col_exp_int = sum(col_exp_int)
        dist = abs(i1 - i2) + abs(j1 - j2) + (exp_rate - 1) * (n_row_exp_int + n_col_exp_int)
        total_dists += dist
    

    return total_dists


if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        lines = f.readlines()


    space = read_space_img(lines)

    galaxy_loc, row_exp, col_exp = expansion(space, expand=True)
    dist_map = calc_dist_pairs_galaxies(galaxy_loc)

    print ('Sum of dists between galaxies:', \
           diff_galaxy_dists(dist_map, galaxy_loc, row_exp, col_exp, exp_rate=1000000))
