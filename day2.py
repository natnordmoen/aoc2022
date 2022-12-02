#!/usr/bin/env python

a = rock = 1
b = paper = 2
c = scissors = 3
lost = 0
draw = 3
won = 6


def find_score_part2(opponent, you):
    x = 0
    y = 3
    z = 6
    if opponent == "A":
        if you == "X":
            return x + scissors
        elif you == "Y":
            return y + rock
        else:
            return z + paper
    elif opponent == "B":
        if you == "X":
            return x + rock
        elif you == "Y":
            return y + paper
        else:
            return z + scissors
    elif opponent == "C":
        if you == "X":
            return x + paper
        elif you == "Y":
            return y + scissors
        else:
            return z + rock

def find_score_part1(opponent, you):
    x = 1
    y = 2
    z = 3
    if opponent == "A":
        if you == "X":
            return x + draw
        elif you == "Y":
            return y + won
        else:
            return z + lost
    elif opponent == "B":
        if you == "X":
            return x + lost
        elif you == "Y":
            return y + draw
        else:
            return z + won
    elif opponent == "C":
        if you == "X":
            return x + won
        elif you == "Y":
            return y + lost
        else:
            return z + draw  


def solve():
    total_score = 0
    with open("day2_input", "r") as f:
        for line in f:
            total_score += find_score_part2(line.split()[0], line.split()[1])

    return total_score, 0

def day2():
    results = solve()
    print("Part 1: ", results[0])
    print("Part 2: ", 0)

day2()