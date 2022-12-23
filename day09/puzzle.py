import os
from collections import defaultdict, deque
import itertools
import copy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from aocd import get_data

def update_position(head_pos, follow_pos):
    ht_dist = head_pos - follow_pos
    if np.max(np.abs(ht_dist)) > 1:
        follow_pos += np.sign(ht_dist)
    return follow_pos

def main():
    data = get_data(day=9, year=2022).split('\n')
    visited = [(0,0)]
    long_visited = [(0,0)]
    head_loc = np.array([0, 0])
    tail_loc = np.array([0, 0])
    dir_dict = {'R': np.array([1, 0]), 'L': np.array([-1, 0]), 'U': np.array([0, 1]), 'D': np.array([0, -1])} #cartesian, not matrix
    long_rope = {}
    for rope_num in range(10):
        long_rope[rope_num] = np.array([0, 0])
    for instruction in data:
        direction, step_amnt = instruction.split(' ')
        for mvi in range(int(step_amnt)):
            head_loc += dir_dict[direction]
            tail_loc = update_position(head_loc, tail_loc)
            long_rope[0] += dir_dict[direction]
            for rn in range(9):
                long_rope[rn + 1] = update_position(long_rope[rn], long_rope[rn + 1])
            if tuple(tail_loc) not in visited:
                visited.append(tuple(tail_loc))
            if tuple(long_rope[9]) not in long_visited:
                long_visited.append(tuple(long_rope[9]))
    print('Star 1:', len(visited))
    print('Star 2:', len(long_visited))





if __name__== main():
    main()
