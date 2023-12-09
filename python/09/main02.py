'''
    Advent of Code 2023
    2023 December 09
    Frank Schoeneman

'''

def oasis_predict(oasis):

    '''
       calc recursive deltas until base (0)
       compute next delta returning through recursion until end
       return predicted value for line by adding delta and last val
       return list of ONLY final pred values from each line
    '''
    def get_next(line):

        if all(d == 0 for d in line):#sum(line) == 0:
           return 0 

        diffs = [ line[i+1] - line[i] for i in range(len(line) - 1) ]

        return line[-1] + get_next(diffs) 

    def predict_next(line):

        res = get_next(line)
        pred_val = line[-1] + res[-1]
        return pred_val 

    # for Part Two, just reverse each line and solve the same problem
    oasis = [list(map(int, line.strip().split()[::-1])) for line in oasis]
    

    return list(map(get_next, oasis))



if __name__ == "__main__":


    with open('input.txt', 'r') as f:
        oasis = f.readlines()


    print ("Sum of extrapolated values:", sum(oasis_predict(oasis)))
