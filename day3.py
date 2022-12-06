#!/usr/bin/env python
import string


def create_decode_dict():
    priorities = {}
    for k, v in zip(list(string.ascii_lowercase), range(1, 27)):
        priorities[k] = v
    for k, v in zip(list(string.ascii_uppercase), range(27, 53)):
        priorities[k] = v
    return priorities


def calculate_score_part1(errors, priorities):
    score = 0
    for e in errors:
        score += priorities[e]
    return score

def calculate_score_part2(errors, priorities):
    score = 0
    for e in [item for sublist in errors for item in sublist]:
        score += priorities[e]
    return score

def find_same_item(errors):
    return list(set.intersection(*map(set, errors)))


def solve():
    errors_part1 = []
    errors_part2 = []
    priorities = create_decode_dict()
    group_of_three = []
    with open("day3_input", "r") as f:
        for line in f:            
            letters = [l for l in line.strip()]
            errors_part1.append(find_same_item([letters[:len(letters)//2], letters[len(letters)//2:]])[0])
            if len(group_of_three) == 3:
                errors_part2.append(find_same_item(group_of_three))
                group_of_three = []
            group_of_three.append(letters)
        errors_part2.append(find_same_item(group_of_three))
            
    return calculate_score_part1(errors_part1, priorities), calculate_score_part2(errors_part2, priorities)

def day3():
    results = solve()
    print("Part 1: ", results[0])
    print("Part 2: ", results[1])

day3()