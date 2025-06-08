import random


class DiceRoll:
    def __init__(self):
        self.dice = [0] * 5

    def roll_dice(self):
        self.dice = [random.randint(1, 6) for _ in range(5)]

    def reroll_dice(self, indices):
        for idx in indices:
            self.dice[idx] = random.randint(1, 6)

    def get_result(self) -> list[int]:
        return self.dice
