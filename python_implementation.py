#!/usr/bin/env python3.9

import random


consideration = []


def roll_dice(sides=6):
    return random.randint(1, sides)


def all_same(container: list[int]):
    if not(container):
        return False
    top = container[0]
    for x in container[1:]:
        if not(x == top):
            return False
    return True


class Player:
    def __init__(self, name: str):
        self.name = name
        self.unconditional_winner = False
        self.overflow = False
        self.position = 0  # where they are on the board
        self.complete_iteration = 0  # have the completely went around the board

    def roll(self, magic: int):
        rolls = [roll_dice() for _ in range(0, 3)]

        self.score = sum(rolls)

        self.unconditional_winner = all_same(rolls) or (self.score == magic)

        if(self.unconditional_winner):
            consideration.append(self)

        if(self.score > magic):
            self.overflow = True

    def reset_score(self):
        self.score, self.unconditional_winner = 0, 0

    def __lt__(self, other):
        return (self.score < other.score)

    def __eq__(self, other):
        return (self.name == other.name) and (id(self) == id(other))


class Cell:
    def __init__(self, is_origin: bool, index: int):
        self.is_origin = is_origin
        self.index = index


class Gameboard:
    def __init__(self, spaces: int, players: list[Player], is_rsg: bool):
        self.spaces = spaces
        self.board = [Cell(False, x) for x in range(0, self.spaces)]
        self.board[0].is_origin = True
        # random seed glitchless. we can do set seed for analysis of the random number generator
        self.is_rsg = is_rsg

    def advance_player(self, direction: int, quantity: int):
        if(direction == -1):
            # move backwards
            print("move backwards")
        else:
            # move forwards
            print("move forwards")


"""
Initial "seed" is set at the beginning of each round
"""

n, m = roll_dice(), roll_dice()

_desired_range = n * m

"""
Here each player will roll
"""


container: list[Player] = [
    Player("Jared"),
    Player("Alex"),
    Player("Chloe")
]

scores = {player.name: 0 for player in container}


def iteration(players: list[Player]):
    for player in players:
        player.roll(_desired_range)

    players = sorted(players)

    scores[players[0].name] += 1

    for player in players:
        player.reset_score()


for x in range(0, 10):
    iteration(container)

print(scores)
# print(f'number intended to hit {_desired_range}, number obtained: {summation}')

