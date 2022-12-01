#!/usr/bin/env python

def day1():
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


max_calories, all_calories = day1() 
sum_top_three = 0
[sum_top_three := sum_top_three + x for x in sorted(all_calories, reverse=True)[:3]]

print("Part 1: ", max_calories)
print("Part 2: ", sum_top_three)
