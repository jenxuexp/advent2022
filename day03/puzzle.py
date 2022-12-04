import os
from collections import defaultdict

import numpy as np
from aocd import get_data



def main():
    orda = ord('a')
    ordA = ord('A')
    data = get_data(day=3, year=2022).split('\n')
    priorities = 0
    for bag in data:
        bag_size = len(bag)
        left = set(bag[:bag_size//2])
        right = set(bag[bag_size//2:])
        extra = list(left.intersection(right))[0]
        priority = get_priority(extra)
        priorities += priority
    print('star1 priorities:', priorities)
    print('data starting length:', len(data))
    badge_priorities = 0
    while len(data)>0:
        bag1 = set(data.pop(0))
        bag2 = set(data.pop(0))
        bag3 = set(data.pop(0))
        print([bag1, bag2, bag3])
        print('length of data', len(data))
        badge = set.intersection(bag1, bag2, bag3)
        print('intersection of data:', badge)
        badge_priority = get_priority(list(badge)[0])
        badge_priorities += badge_priority
    print('star2 priorities:', badge_priorities)


def get_priority(letter):
    if letter.isupper():
        priority = ord(letter) - ord('A') + 27
    else:
        priority = ord(letter) - ord('a') + 1
    return priority

if __name__== main():
    main()
