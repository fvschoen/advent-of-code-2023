
'''
    Advent of Code 2023
    2023 December 08
    
    Frank Schoeneman
'''

def parse_map(lines):

    dirs = list(lines[0].strip())
    nodes = lines[2:]

    parse1 = [node.strip().split('=') for node in nodes]
    nodes  = dict([(node[0].strip(), (node[1].strip().split(',')[0].strip()[1:], 
                                     node[1].strip().split(',')[1].strip()[:-1])) 
                                     for node in parse1])

    return dirs, nodes


def count_steps(nodes, dirs):

    def dir_to_idx(d):

        if d == "R": return 1
        return 0

    dir_idx = list(map(dir_to_idx, dirs))
    num_dirs = len(dir_idx)

    curr_node = "AAA"
    step_count = 0
    curr_idx = 0
    
    while curr_node != "ZZZ":
        curr_node = nodes[curr_node][dir_idx[curr_idx]]
        step_count += 1
        curr_idx += 1
        curr_idx = curr_idx % num_dirs

    return step_count

if __name__ == "__main__":

    with open('input.txt', 'r') as f:
        lines = f.readlines()

    dirs, nodes = parse_map(lines)

    print ("total # steps:", count_steps(nodes, dirs))
