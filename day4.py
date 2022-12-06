#!/usr/bin/env python

def make_ranges(section1, section2):
    pair1, pair2 = section1.split("-"), section2.split("-")
    return list(range(int(pair1[0]), int(pair1[1])+1)), list(range(int(pair2[0]), int(pair2[1])+1))


def solve():
    section1 = section2 = []
    part1 = part2 = 0

    with open("day4_input", "r") as f:
        for line in f:
            splitted = line.split(",")
            section1, section2 = make_ranges(splitted[0], splitted[1])
            
            if set(section1).issubset(section2) or set(section2).issubset(section1):
                part1 += 1
            if set(section1).intersection(section2):
                part2 += 1
            
    return part1, part2

def day4():
    results = solve()
    print("Part 1: ", results[0])
    print("Part 2: ", results[1])

day4()