'''
   Advent of Code 2023
   10 December 2023

   Frank Schoeneman

'''

import itertools

def parse_puzzle(lines):

    puzzle = [list(line.strip()) for line in lines]

    return puzzle

def find_start(puzzle):
    for i in range(len(puzzle)):
        if 'S' in puzzle[i]:
            return i, puzzle[i].index('S')


def bfs(puzzle, S):

    def determine_S(S):

        for dir1, dir2 in itertools.combinations(valid.keys(), 2):
            if puzzle[step(S, dir1)[0]][step(S, dir1)[1]] in valid[dir1] and\
               puzzle[step(S, dir2)[0]][step(S, dir2)[1]] in valid[dir2]:
 
               return list(set(valid[dir1]).intersection(set(valid[dir2])))[0]  

    def node_visited(N, v):
        return N in v
 
    def step(C, D):
        return (C[0] + D[0], C[1] + D[1])

    adj_step = [(-1, 0), (1, 0), (0, -1), (0, 1)] # U, D, L, R or N, S, W, E
    moves = {'|':[(1, 0), (-1, 0)], 
             '-':[(0, 1), (0, -1)], 
             'L':[(0, 1), (-1, 0)],
             'J':[(0, -1), (-1, 0)],
             '7':[(0, -1), (1, 0)], 
             'F':[(0, 1), (1, 0)]}   

    valid = {(0, -1):['|', '7', 'F'],
             (1, 0):['-', '7', 'J'], 
             (0, 1):['|', 'L', 'J'], 
             (-1, 0):['-', 'L', 'F']}

    puzzle[S[0]][S[1]] = determine_S(S)

    q = [S]
    vis = []

    last_C = S
    while q:
        C = q.pop(0)
        pipe = puzzle[C[0]][C[1]]

        # if visited, skip, else mark visited
        if node_visited(C, vis): continue
        vis.append(C)

        for next_j, next_i in moves[pipe]:
            next_C = step(C, (next_j, next_i))
            if next_C != last_C:
               last_C = C
               C = next_C
               q.append(next_C)
               break;

    return len(vis) // 2

if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        puzzle = f.readlines()

    puzzle = parse_puzzle(puzzle)

    S = find_start(puzzle)    

    print ("Length of loop:", bfs(puzzle, S))
