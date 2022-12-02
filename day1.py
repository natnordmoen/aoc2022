#!/usr/bin/env python

def solve():
    f = open("day1_input", "r")
    calories = 0
    all_calories = []
    for line in f.readlines():
        if line not in ['\n', '\r\n']:
            calories += int(line)
        else:
            all_calories.append(calories)
            calories = 0
    return all_calories

def day1():
    all_calories = solution2()
    sum_top_three = 0
    [sum_top_three := sum_top_three + x for x in sorted(all_calories, reverse=True)[:3]]
    print("Part 1: ", sorted(all_calories, reverse=True)[0])
    print("Part 2: ", sum_top_three)

day1()