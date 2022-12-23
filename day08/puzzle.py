import os
from collections import defaultdict, deque
import itertools
import copy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from aocd import get_data

def get_max_trees_in_dir(forest, rowcol, count_dir):
    count = 0
    tree_height = forest[rowcol[0], rowcol[1]]
    row = rowcol[0] + count_dir[0]
    col = rowcol[1] + count_dir[1]
    found_max = False
    while row >= 0 and col >= 0 and row < forest.shape[0] and col < forest.shape[1] and not found_max:
        next_value = forest[row, col]
        count += 1
        found_max = (next_value >= tree_height)
        row += count_dir[0]
        col += count_dir[1]
    return count

def main():
    # Star 1
    data = get_data(day=8, year=2022).split('\n')
    data_list = np.array([[int(s) for s in line] for line in data])
    data_list_inv = np.fliplr(np.flipud(data_list))
    tl_df = pd.DataFrame(data_list)
    br_df = pd.DataFrame(data_list_inv)
    tl_vis = (data_list > np.roll(tl_df.cummax(axis=0).to_numpy(), 1, axis=0)) | (data_list > np.roll(tl_df.cummax(axis=1).to_numpy(), 1, axis=1))
    br_vis = (data_list_inv > np.roll(br_df.cummax(axis=0).to_numpy(), 1, axis=0)) | (data_list_inv > np.roll(br_df.cummax(axis=1).to_numpy(), 1, axis=1))
    vis_from_outside = tl_vis | np.fliplr(np.flipud(br_vis))
    vis_from_outside[[0, -1], :] = 1
    vis_from_outside[:, [0, -1]] = 1
    print(np.sum(vis_from_outside.astype(int)))

    # Doing star 2 the silly way because max trees do 2D connectivity :(
    distances = np.zeros_like(data_list)
    forest_shape = np.shape(data_list)
    count_dirs = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    for row in range(forest_shape[0]):
        for col in range(forest_shape[1]):
            multiplier = 1
            for count_dir in count_dirs:
                multiplier *= get_max_trees_in_dir(data_list, (row, col), count_dir)
            distances[row, col] = multiplier
    print('Star 2:', np.max(distances))




if __name__== main():
    main()
