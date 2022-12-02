#!/usr/bin/env python

rock = 1
paper = 2
scissors = 3
lost = 0
draw = 3
won = 6


def part2(opponent, you):
    if opponent == "A":
        if you == "X":
            return lost + scissors
        elif you == "Y":
            return draw + rock
        else:
            return won + paper
    elif opponent == "B":
        if you == "X":
            return lost + rock
        elif you == "Y":
            return draw + paper
        else:
            return won + scissors
    elif opponent == "C":
        if you == "X":
            return lost + paper
        elif you == "Y":
            return draw + scissors
        else:
            return won + rock

def part1(opponent, you):
    if opponent == "A":
        if you == "X":
            return rock + draw
        elif you == "Y":
            return paper + won
        else:
            return scissors + lost
    elif opponent == "B":
        if you == "X":
            return rock + lost
        elif you == "Y":
            return paper + draw
        else:
            return scissors + won
    elif opponent == "C":
        if you == "X":
            return rock + won
        elif you == "Y":
            return paper + lost
        else:
            return scissors + draw  

def find_score(isPart1, opponent, you):
    if isPart1:
        return part1(opponent, you)
    else:
        return part2(opponent, you)


def solve():
    total_score_part1 = 0
    total_score_part2 = 0
    with open("day2_input", "r") as f:
        for line in f:
            total_score_part1 += find_score(True, line.split()[0], line.split()[1])
            total_score_part2 += find_score(False, line.split()[0], line.split()[1])

    return total_score_part1, total_score_part2

def day2():
    results = solve()
    print("Part 1: ", results[0])
    print("Part 2: ", results[1])

day2()