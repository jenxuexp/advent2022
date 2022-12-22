import os
from collections import defaultdict, deque
import itertools

import numpy as np
from aocd import get_data

class FileNode:
    def __init__(self, parent, name, size):
        self.parent = parent
        self.name = name
        self.size = size

class TreeNode:
    def __init__(self, parent, name):
        self.parent = parent
        self.name = name
        self.child_files = []
        self.child_dirs = []
        self.size = 0
        self.parsed_dirs = []

    def change_dir(self, child_dir_name):
        if child_dir_name == '..':
            return self.parent
        if child_dir_name == '/':
            return ROOT
        for child_dir in self.child_dirs:
            if child_dir.name == child_dir_name:
                return child_dir
        print("Did not find child directory in parent, manually creating")
        self.child_dirs.append(TreeNode(self, child_dir_name))
        return self.child_dirs[-1]

    def populate_children(self, command_str):
        command_list = command_str.split('\n')
        for ls_item in command_list[1:]:
            fname = ls_item.split(' ')[1]
            if ls_item[:3] == 'dir':
                if fname not in [child.name for child in self.child_dirs]:
                    self.child_dirs.append(TreeNode(self, fname))
            else:
                filesize = int(ls_item.split(' ')[0])
                if fname not in [child.name for child in self.child_files]:
                    self.child_files.append(FileNode(self, fname, filesize))
                    self.size += filesize


def build_tree_from_input(input_str):
    ROOT = TreeNode(None, 'root')
    commands = input_str.split('\n$ ')
    current_dir = ROOT
    for command in commands[1:]:
        print('Command:', command)
        if 'cd' in command[:2]:
            print('previous directory = ', current_dir.name)
            current_dir = current_dir.change_dir(command.split(' ')[1].strip())
            print('current directory = ', current_dir.name)
        else: # it is ls
            current_dir.populate_children(command)
    return ROOT

def parse_sizes(tree):
    """Starting at root, and assuming that the tree was built
    so that the individual file sizes have already been summed in a directory,
    traverse the tree and output all individual file sizes as well as directory sizes in a list"""
    child_dirs_list = [tree.child_dirs]
    sizen = []
    while len(child_dirs_list) > 0:
        working_dir_list = child_dirs_list.pop()
        working_dir = working_dir_list.pop()
        if len(working_dir.child_dirs) > 0:
            working_dir_list.append(working_dir)
            next_dir_list = working_dir.child_dirs
            child_dirs_list.append(working_dir_list)
            child_dirs_list.append(next_dir_list)
        else: # the working directory has no children that are unparsed, so we pop up its size to its parent and move it to the
            if working_dir.name != 'root':
                working_dir.parent.size += working_dir.size
                working_dir.parent.parsed_dirs.append(working_dir)
            sizen.append(working_dir.size)
            if working_dir_list:
                child_dirs_list.append(working_dir_list)
    return sizen

available_space = 70000000
needed_unused_space = 30000000
max_space_used = available_space - needed_unused_space

def main():
    data = get_data(day=7, year=2022)
    tree = build_tree_from_input(data)
    file_sizes = np.array(parse_sizes(tree))
    print(file_sizes)
    large_file_sum = np.sum(file_sizes[file_sizes <= 100000 ])
    print('Star 1 size sum:', large_file_sum)
    needed_deletion = tree.size - max_space_used
    candidate_deletions = file_sizes[file_sizes >= needed_deletion]
    print('Smallest valid size for deletion:', np.min(candidate_deletions))

if __name__== main():
    main()
