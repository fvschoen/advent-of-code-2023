"""
Advent of Code 2023
2023 December 01

Frank Schoeneman

"""

def extract_cal_code(line):

    only_digits = [this_char for this_char in line \
                                    if this_char.isdigit()]

    first_digit = only_digits[0]
    last_digit  = only_digits[-1]

    return int(first_digit + last_digit)


if __name__ == "__main__":

    input_file = "input.txt"

    with open(input_file, 'r') as f:
        cal_lines = f.readlines()

    print( sum( map(extract_cal_code, cal_lines) ) )
