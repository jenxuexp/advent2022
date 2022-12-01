import os
from collections import deque

import numpy as np

def main():
    max_cals = parse_max_cals('day1_input.txt')
    print('star 1 max calories:', max_cals)
    sum_cals = parse_3max('day1_input.txt')
    print('star 2 top 3 calorie carrier sum:', sum_cals)

def parse_max_cals(fname):
    max_cals = 0
    current_cals = 0
    for line in open(fname):
        if line == '\n':
            max_cals = max(max_cals, current_cals)
            current_cals = 0
        else:
            current_cals += float(line.strip())
    return max_cals

def parse_3max(fname):
    max_list = np.zeros(3)
    current_cals = 0
    for line in open(fname):
        if line == '\n':
            max_list = check_replace_min(max_list, current_cals)
            current_cals = 0
        else:
            current_cals += float(line.strip())
    sum_cals = np.sum(max_list)
    return sum_cals

def check_replace_min(max_list, new_val):
    min_ind = np.argmin(max_list)
    if new_val > max_list[min_ind]:
        max_list[min_ind] = new_val
    return max_list

if __name__== main():
    main()
