import os
from collections import defaultdict

import numpy as np

WIN = 6
LOSE = 0
DRAW = 3

ROCK = 1
PAPER = 2
SCISSOR = 3


def get_scoring_dictionary():
    score_dict = defaultdict(lambda: defaultdict(int))
    score_dict['A']['Y'] = WIN
    score_dict['A']['X'] = DRAW
    score_dict['B']['Z'] = WIN
    score_dict['B']['Y'] = DRAW
    score_dict['C']['X'] = WIN
    score_dict['C']['Z'] = DRAW
    round_dict = {'X': 1, 'Y': 2, 'Z': 3}
    return score_dict, round_dict

def get_second_scoring_dictionary():
    score_dict = defaultdict(lambda: defaultdict(lambda: 1))
    score_dict['A']['Z'] = PAPER
    score_dict['A']['X'] = SCISSOR
    score_dict['B']['Y'] = PAPER
    score_dict['B']['Z'] = SCISSOR
    score_dict['C']['X'] = PAPER
    score_dict['C']['Y'] = SCISSOR
    round_dict = {'X': LOSE, 'Y': DRAW, 'Z': WIN}
    return score_dict, round_dict

def get_score(score_dict, round_dict, line):
    opp, mine = line.split(' ')
    return score_dict[opp][mine] + round_dict[mine]

def parse_rules(fname):
    score_dict, round_dict = get_scoring_dictionary()
    score_dict2, round_dict2 = get_second_scoring_dictionary()
    score = 0
    score2 = 0
    for line in open(fname):
        score += get_score(score_dict, round_dict, line.strip())
        score2 += get_score(score_dict2, round_dict2, line.strip())
    return score, score2

def main():
    print(parse_rules('day2_input.txt'))


if __name__== main():
    main()
