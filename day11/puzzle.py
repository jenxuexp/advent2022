import os
from collections import defaultdict, deque
import itertools
import copy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from aocd import get_data

class Monkey:
    def __init__(self, init_str, worry_divider=3):
        descriptor = init_str.split('\n')
        self.id = int(descriptor[0][-2])
        self.items = deque([int(item_id.strip()) for item_id in descriptor[1].strip().split(':')[1].split(',')])
        self.op_str = descriptor[2].strip().split('= ')[1]
        self.test_divisor = int(descriptor[3].split('divisible by ')[1])
        self.true_recipient = int(descriptor[4][-1])
        self.false_recipient = int(descriptor[5][-1])
        self.num_inspections = 0
        self.worry_divider = worry_divider

    def take_turn(self, monkey_list, gcm=None):
        while len(self.items) > 0:
            self.num_inspections += 1
            old = self.items.popleft()
            new = eval(self.op_str) // self.worry_divider
            if gcm:
                new = new % gcm
            if new % self.test_divisor == 0:
                monkey_list[self.true_recipient].items.append(new)
            else:
                monkey_list[self.false_recipient].items.append(new)
        return monkey_list


def main():
    data = get_data(day=11, year=2022).split('\n\n')
    monkey_list = []
    for monkey_str in data:
        monkey_list.append(Monkey(monkey_str))
    for round_num in range(20):
        for mind in range(len(monkey_list)):
            monkey_list = monkey_list[mind].take_turn(monkey_list)
    monkey_activity = [monkey.num_inspections for monkey in monkey_list]
    print('Star 1 Monkey Business:', np.prod(sorted(monkey_activity)[-2:]))
    monkey_list2 = []
    for monkey_str in data:
        monkey_list2.append(Monkey(monkey_str, worry_divider=1))
    max_multiple = np.prod([monkey.test_divisor for monkey in monkey_list])
    for round_num in range(10000):
        for mind in range(len(monkey_list2)):
            monkey_list2 = monkey_list2[mind].take_turn(monkey_list2, gcm=max_multiple)
    long_monkey_activity = [monkey.num_inspections for monkey in monkey_list2]
    print('Star 2 Monkey Business:', np.prod(sorted(long_monkey_activity)[-2:]))


if __name__== main():
    main()
