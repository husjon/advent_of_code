#!/usr/bin/env python
import os
import re

def find_numbers(line: str):
    x = re.sub('[a-z]+', '', line)
    return int(f'{x[0]}{x[-1]}')

def solve(input_content: str):
    numbers = []
    for line in input_content.splitlines():
        number = find_numbers(line)
        numbers.append(number)

    return sum(numbers)

if __name__ == '__main__':
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    with open('./input.txt', 'r', encoding='utf-8') as f:
        INPUT = f.read()

    solution = solve(input_content=INPUT)
    print(solution)
