#!/usr/bin/env python
import string


def create_decode_dict():
    priorities = {}
    for k, v in zip(list(string.ascii_lowercase), range(1, 27)):
        priorities[k] = v
    for k, v in zip(list(string.ascii_uppercase), range(27, 53)):
        priorities[k] = v
    return priorities


def calculate_score(errors, priorities):
    score = 0
    for e in errors:
        score += priorities[e]
    return score


def find_same_item(comp1, comp2):
    return list(set(comp1).intersection(comp2))


def solve():
    errors = []
    priorities = create_decode_dict()
    with open("day3_input", "r") as f:
        for line in f:
            letters = [l for l in line]
            errors.append(find_same_item(letters[:len(letters)//2], letters[len(letters)//2:])[0])

    return calculate_score(errors, priorities)

def day3():
    results = solve()
    print("Part 1: ", results)
    print("Part 2: ", 0)

day3()