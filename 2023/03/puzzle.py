#!/usr/bin/env python
import os
import re


def solve(input_content: str):
    grid = []

    # Pad the grid
    for line in input_content.splitlines():
        grid.append(["."] + [*line] + ["."])

    grid_width = len(grid[0])
    grid.insert(0, ["."] * grid_width)
    grid.append(["."] * grid_width)

    # Find the numbers in the grid with position
    pattern = re.compile(r"(\d+)", flags=re.X)

    parts = []
    for line_number, line in enumerate(grid):
        for match in re.finditer(pattern=pattern, string="".join(line)):
            pos_min, pos_max = match.span()
            number = int(match.group())
            is_part = False
            for y in range(line_number - 1, line_number + 2):
                for x in range(pos_min - 1, pos_max + 1):
                    pos = grid[y][x]
                    if pos not in "1234567890.":
                        is_part = True
                        parts.append(number)
                        break
                if is_part:
                    break

    return sum(parts)


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    with open("./input.txt", "r", encoding="utf-8") as f:
        INPUT = f.read()

    solution = solve(input_content=INPUT.strip())
    print(solution)
