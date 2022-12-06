import os
from collections import defaultdict, deque
import itertools

import numpy as np
from aocd import get_data

MARKER_SIZE = 4
MESSAGE_SIZE = 14

def check_for_marker(gibberish, marker_size):
    for marker_pos in range(len(gibberish) - marker_size):
        marker_candidate = set(gibberish[marker_pos:(marker_pos + marker_size)])
        if len(marker_candidate) == marker_size:
            return (marker_pos + marker_size)
            break

def main():
    data = get_data(day=6, year=2022)
    print('Star 1 length:', check_for_marker(data, MARKER_SIZE))
    print('Star 2 length:', check_for_marker(data, MESSAGE_SIZE))

if __name__== main():
    main()
