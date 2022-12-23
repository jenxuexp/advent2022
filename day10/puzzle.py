import os
from collections import defaultdict, deque
import itertools
import copy

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from aocd import get_data

class CPU:
    def __init__(self):
        self.cycle_num = 0
        self.x_reg = 1
        self.cycle_tracker = []
        self.register_tracker = []
        self.cycle_tracker.append(0)
        self.register_tracker.append(1)

    def addx(self, value):
        self.x_reg += value
        self.cycle_num += 2
        self.cycle_tracker.append(self.cycle_num + 1)
        self.register_tracker.append(self.x_reg)

    def noop(self):
        self.cycle_num += 1

    def get_x_at_cycle(self, cycle_num):
        last_cycle_update = np.argmax(np.array(self.cycle_tracker) > cycle_num) - 1
        return self.register_tracker[last_cycle_update]

def main():
    data = get_data(day=10, year=2022).split('\n')
    cycles_of_interest = [20, 60, 100, 140, 180, 220]
    cpu = CPU()
    for command in data:
        if command[:4] == 'addx':
            cpu.addx(int(command.split(' ')[1]))
        else:
            cpu.noop()
    sum_star1 = 0
    for cn in cycles_of_interest:
        sum_star1 += cpu.get_x_at_cycle(cn) * cn
    print('Star 1:', sum_star1)

    pixel_val = []
    for dn in range(240):
        x_reg_val = cpu.get_x_at_cycle(dn + 1)
        hpos = dn % 40
        if hpos <= x_reg_val + 1 and hpos >= x_reg_val - 1:
            pixel_val.append('#')
        else:
            pixel_val.append('.')
    crt = np.reshape(np.array(pixel_val), (6, 40))
    for line in crt:
        print(''.join(list(line)))






if __name__== main():
    main()
