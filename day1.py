#!/usr/bin/env python

from functools import reduce

def solve():
    f = open("day1_input", "r")
    calories = 0
    max_calories = 0
    all_calories = []
    for line in f.readlines():
        if line not in ['\n', '\r\n']:
            calories += int(line)
        else:
            all_calories.append(calories)
            if calories > max_calories:
                max_calories = calories
                calories = 0
            else:
                calories = 0
    return max_calories, all_calories




def day1():
    return solve()


results = day1() 
total = 0
[total := total + x for x in sorted(results[1], reverse=True)[:3]]

print("Part 1: ", results[0])
print("Part 2: ", total)
