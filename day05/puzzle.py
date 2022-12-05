import os
from collections import defaultdict, deque
import itertools

import numpy as np
from aocd import get_data


def make_boxes_from_string(box_list, num_stacks):
    box_stacks = defaultdict(lambda: deque())
    for box_row in box_list:
        box_row = box_row + ' ' # can be more clever here, but meh
        for stack_num in range(num_stacks):
            crate = box_row[stack_num*4:(stack_num+1)*4].strip('[ ]')
            if crate:
                box_stacks[stack_num].append(crate) # left side of deque will be "up"
    return box_stacks

def move_boxen(instruction, box_stacks):
    mo = instruction.split(' ')
    num_boxen = int(mo[1])
    from_id = int(mo[3]) - 1
    to_id = int(mo[5]) - 1
    for move_num in range(num_boxen):
        box_stacks[to_id].appendleft(box_stacks[from_id].popleft())
    return box_stacks

def advanced_move_boxen(instruction, box_stacks):
    mo = instruction.split(' ')
    num_boxen = int(mo[1])
    from_id = int(mo[3]) - 1
    to_id = int(mo[5]) - 1
    move_crates = deque()
    for move_num in range(num_boxen):
        move_crates.appendleft(box_stacks[from_id].popleft())
    box_stacks[to_id].extendleft(move_crates)
    return box_stacks

def main():
    data = get_data(day=5, year=2022).split('\n\n')
    boxen = data[0].split('\n')
    instructions=data[1].split('\n')
    num_stacks = 9
    box_stacks = make_boxes_from_string(boxen[:-1], num_stacks)
    star2_boxes = make_boxes_from_string(boxen[:-1], num_stacks)
    for instruction in instructions:
        box_stacks = move_boxen(instruction, box_stacks)
        star2_boxes = advanced_move_boxen(instruction, star2_boxes)
    message = ''
    upgraded_message = ''
    for column in range(num_stacks):
        message += box_stacks[column].popleft()
        upgraded_message += star2_boxes[column].popleft()
    print('Star 1 message:', message)
    print('Star 2 message:', upgraded_message)


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
