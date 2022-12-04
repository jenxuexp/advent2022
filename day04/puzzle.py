import os
from collections import defaultdict

import numpy as np
from aocd import get_data



def main():
    data = get_data(day=4, year=2022).split('\n')
    redundancies = 0
    overlaps = 0
    for pair in data:
        sections = [[int(val) for val in assignment.split('-')] for assignment in pair.split(',')]
        group1 = set(np.arange(sections[0][0], sections[0][1] + 1))
        group2 = set(np.arange(sections[1][0], sections[1][1] + 1))
        group_union = group1.union(group2)
        group_intersect = group1.intersection(group2)
        if group_union == group1 or group_union == group2:
            # print('Found redundancy')
            # print(sections)
            print(pair)
            redundancies += 1
        if group_intersect:
            overlaps += 1
    print('star1 redundancies:', redundancies)
    print('data starting length:', len(data))
    print('star 2 overlaps:', overlaps)
    # badge_priorities = 0
    # while len(data)>0:
    #     bag1 = set(data.pop(0))
    #     bag2 = set(data.pop(0))
    #     bag3 = set(data.pop(0))
    #     print([bag1, bag2, bag3])
    #     print('length of data', len(data))
    #     badge = set.intersection(bag1, bag2, bag3)
    #     print('intersection of data:', badge)
    #     badge_priority = get_priority(list(badge)[0])
    #     badge_priorities += badge_priority
    # print('star2 priorities:', badge_priorities)


if __name__== main():
    main()
