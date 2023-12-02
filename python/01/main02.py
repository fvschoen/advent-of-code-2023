"""
 Advent of Code 2023
 2023 December 01

 Frank Schoeneman

"""


def is_prefix(substring, word_list):

    for word in word_list:
        if word.startswith(substring) and word != substring: return True
    return False

def extract_cal_code(line):

    s_ptr = 0
    f_ptr = 0
    n = len(line)
    
    only_digits = []
    digits_with_idx = []

    while s_ptr < n and f_ptr < n:

        if line[s_ptr].isdigit(): 
            only_digits.append(line[s_ptr])
            digits_with_idx.append((s_ptr, line[s_ptr]))
            s_ptr += 1
       
        else: 
            substring = line[s_ptr:f_ptr+1]

            if is_prefix(substring, digit_words.keys()):
                f_ptr += 1
            elif substring in digit_words.keys():
                only_digits.append(digit_words[substring])
                digits_with_idx.append((s_ptr, substring))
                s_ptr = f_ptr
                f_ptr = s_ptr + 1
        
            else:
                s_ptr = s_ptr + 1
                f_ptr = s_ptr + 1

    first_digit = only_digits[0]
    last_digit  = only_digits[-1]

    return int(first_digit + last_digit)


if __name__ == "__main__":

    input_file = "input.txt"

    digit_words = {'one':'1', 'two':'2', 'three':'3', 'four':'4', \
                   'five':'5', 'six':'6', 'seven':'7', 'eight':'8', \
                   'nine':'9'}

    with open(input_file, 'r') as f:
        cal_lines = f.readlines()
 
    print ('Final Sum:') 
    print( sum( map(extract_cal_code, cal_lines) ) )
