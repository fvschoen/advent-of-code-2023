"""

Advent of Code 2023
2023 December 03

Frank Schoeneman

"""

def find_parts(s_grid):

    symbols = "!@#$%^&*()-+?_=,<>/"

    n, m = len(s_grid), len(s_grid[0])
    num_elem = n * m

    memo = [[0 for _ in range(m)] for _ in range(n)]

    adj_dirs = [[0, -1], [0, 1], [-1, 0], [1, 0],\
               [-1, -1], [1, -1], [-1, 1], [1, 1]]
    
    part_nums = []
 
    for I in range(num_elem):
        i, j = I // n, I % m

        if s_grid[i][j] in symbols: 
            # found a symbol, look in adj_dir for digits
            for adj_dir in adj_dirs:
                if  not (0 <= i + adj_dir[0] < n) or not (0 <= j + adj_dir[1] < m): continue;
 
                temp_i, temp_j = i + adj_dir[0], j + adj_dir[1]

                if s_grid[temp_i][temp_j].isdigit() and \
                   memo[temp_i][temp_j] == 0:

                    num_start, num_end = temp_j, temp_j
                    memo[temp_i][temp_j] = 1

                    while num_start > 0:
                        if s_grid[temp_i][num_start - 1].isdigit(): 
                            num_start -= 1
                            memo[temp_i][num_start] = 1
                        else: break;

                    while num_end < m - 1:
                        if s_grid[temp_i][num_end + 1].isdigit(): 
                            num_end += 1
                            memo[temp_i][num_end] = 1
                        else: break;

                    part_nums.append( "".join( s_grid[temp_i][num_start:(1 + num_end)] ) )

    return part_nums


if __name__ == "__main__":

    input_file = "input.txt"

    with open(input_file, 'r') as f:
        schematic = f.readlines()

    schematic_grid = [ [ char for char in line.replace('\n', '') ] for line in schematic]

    print ( "Total Part Numbers:", sum( map( int, find_parts(schematic_grid) ) ) )
