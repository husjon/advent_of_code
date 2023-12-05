#!/usr/bin/env python
import os
import re

PATTERN = re.compile(r"(?=(one|two|three|four|five|six|seven|eight|nine|[1-9]))")
NUMBER_MAPPING = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}


def parse_number(number: int):
    if number in NUMBER_MAPPING:
        return NUMBER_MAPPING[number]

    return int(number)


def find_numbers(line: str):
    # Builds a list of all numbers in a string
    # `nhchm9dtkbpkbtwonbfnjfgctwosevenlvxvvtlmzptzpc` becomes:
    #       ^        ^          ^  ^
    # ['9', 'two', 'two', 'seven']
    match = re.findall(pattern=PATTERN, string=line.strip())

    first = match[0]
    last = match[-1]
    first_number = parse_number(first)
    last_number = parse_number(last)

    return int(f"{first_number}{last_number}")


def solve(input_content: str):
    numbers = []
    for line in input_content.splitlines():
        numbers.append(find_numbers(line))

    return sum(numbers)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    with open("./input.txt", "r", encoding="utf-8") as f:
        INPUT = f.read().strip()

    solution = solve(input_content=INPUT)
    print(solution)
