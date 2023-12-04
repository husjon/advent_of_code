#!/usr/bin/env python
import os


def parse_cards(line: str):
    _, data_raw = line.split(":")
    winning_cards, my_cards = data_raw.split("|")
    return winning_cards.split(), my_cards.split()


def get_winning_cards(cards):
    winning, current = cards

    winning_cards = []
    for card in current:
        if card in winning:
            winning_cards.append(card)
    return winning_cards


def solve(input_content: str):
    score = 0
    for line in input_content.strip().splitlines():
        card_sequence = parse_cards(line)
        cards = get_winning_cards(card_sequence)
        count = len(cards)
        if count > 0:
            score += 2 ** (count - 1)

    return score


if __name__ == "__main__":
    os.chdir(os.path.dirname(os.path.realpath(__file__)))
    with open("./input.txt", "r", encoding="utf-8") as f:
        INPUT = f.read()
    with open("./input.test.txt", "r", encoding="utf-8") as f:
        INPUT = f.read()

    solution = solve(input_content=INPUT)
    print(solution)
