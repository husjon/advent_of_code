#!/usr/bin/env python
import os


def solve(input_content:str):
    lines = input_content.split('\n')

    elves = []
    calories = 0

    for line in lines:
        if line == '':
            calories = 0
            continue

        calorie = int(line)
        calories += calorie
        elves.append(calories)

    largest = max(elves)

    top_3 = sorted(elves, reverse=True)[:3]

    return {
        'largest': largest,
        'top_3_total': sum(top_3),
    }


if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    with open('./input.txt', 'r', encoding='utf-8') as f:
        INPUT = f.read()

    solution = solve(input_content=INPUT)
    print(solution)
