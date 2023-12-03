#!/usr/bin/env python
import os
import re

PATTERN = re.compile(r"Game \d+: (?P<set1>.*?); (?P<set2>.*?); (?P<set3>.*?)")
THRESHOLD = {"red": 12, "green": 13, "blue": 14}


def parse_games(input_data: str):
    input_data = re.sub(r"Game \d+: ", "", input_data)
    lines = input_data.strip().split("\n")

    games = []
    for i, line in enumerate(lines):
        blocks = {"id": i + 1, "red": 0, "green": 0, "blue": 0}
        for _set in line.split("; "):
            for combi in _set.split(", "):
                amount, color = combi.split()

                if int(amount) > blocks[color]:
                    blocks[color] = int(amount)

        games.append(blocks)

    return games


def solve(input_content: str):
    games = parse_games(input_data=input_content)

    power_sum = 0
    for g in games:
        power = g["red"] * g["green"] * g["blue"]
        power_sum += power

    return power_sum


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    with open("./input.txt", "r", encoding="utf-8") as f:
        INPUT = f.read()

    # INPUT = """
    # Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
    # Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
    # Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
    # Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
    # Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
    solution = solve(input_content=INPUT)
    print(solution)
