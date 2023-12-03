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
    valid_games = []
    for game in games:
        if (
            game["red"] <= THRESHOLD["red"]
            and game["green"] <= THRESHOLD["green"]
            and game["blue"] <= THRESHOLD["blue"]
        ):
            valid_games.append(game)

    valid_ids = []
    for game in valid_games:
        valid_ids.append(game["id"])

    return sum(valid_ids)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    with open("./input.txt", "r", encoding="utf-8") as f:
        INPUT = f.read()

    solution = solve(input_content=INPUT)
    print(solution)
