#!/usr/bin/env python
import string


def create_lookup_dict(crates_number):
    places = list(range(1, 35, 4)) # indices
    crates_indices = dict()

    i = 0
    for key in range(1, crates_number+1):
        crates_indices[places[i]] = key
        i += 1
    return crates_indices

def make_crates(input, crates_number, lookup_dict):
    crates = dict()

    #init empty dict with correct keys
    for key in range(1, crates_number+1):
        crates[key] = []

    for line in input:
        indices = [i for i, e in enumerate(line) if e in string.ascii_uppercase]
        for i in indices:
            crates[lookup_dict[i]].append(line[i])

    return crates

def apply_instruction(crates, instruction):
    details = instruction.split(' ')
    how_many = int(details[1])
    from_crate = int(details[3])
    to_crate = int(details[5])

    for c in range(1, how_many+1):
        crates[to_crate].insert(0, crates[from_crate][0])
        crates[from_crate].pop(0)

    return crates

def find_top_crates(crates):
    top = ""
    for k, v in crates.items():
        top+=v[0]
    return top

def solve():
    f = open("day5_input", "r")
    lines = f.readlines()

    empty_line_index = lines.index('\n')
    crates_number = int(lines[empty_line_index-1].strip().split()[-1])

    lookup_dict = create_lookup_dict(crates_number)

    # {1: [N, Z], 2: [D, C, M], 3: [P]} the top block is at index 0
    crates = make_crates(lines[:empty_line_index-1], crates_number, lookup_dict) 

    instructions = lines[empty_line_index+1:]
    for instruction in instructions:
        crates = apply_instruction(crates, instruction)

    top_crates = find_top_crates(crates)

    return top_crates, 0

def day5():
    results = solve()
    print("Part 1: ", results[0])
    print("Part 2: ", results[1])

day5()