from collections import Counter
from enum import IntEnum


class Ranking(IntEnum):
    NOTHING = 0
    PAIR = 1
    TWO_PAIRS = 2
    THREE_OF_A_KIND = 3
    FIVE_HIGH_STRAIGHT = 4
    SIX_HIGH_STRAIGHT = 5
    FULL_HOUSE = 6
    FOUR_OF_A_KIND = 7
    FIVE_OF_A_KIND = 8


class HandEvaluator:
    def evaluate_hand(self, hand: list[int]) -> Ranking:
        counts = Counter(hand).values()
        # Nothing — five mismatched dice forming no sequence longer than four.
        if len(hand) == len(counts):
            return Ranking.NOTHING
        # Pair — two dice showing the same value.
        if sorted(counts) == [1, 1, 1, 2]:
            return Ranking.PAIR
        # Two Pairs — two pairs of dice, each showing the same value.
        if sorted(counts) == [1, 2, 2]:
            return Ranking.TWO_PAIRS
        # Three-of-a-Kind — three dice showing the same value.
        if sorted(counts) == [1, 1, 3]:
            return Ranking.THREE_OF_A_KIND
        # Five High Straight — dice showing values from 1 through 5, inclusive.
        if sorted(hand) == [1, 2, 3, 4, 5]:
            return Ranking.FIVE_HIGH_STRAIGHT
        # Six High Straight — dice showing values from 2 through 6, inclusive.
        if sorted(hand) == [2, 3, 4, 5, 6]:
            return Ranking.SIX_HIGH_STRAIGHT
        # Full House — Pair of one value and Three-of-a-Kind of another.
        if sorted(counts) == [2, 3]:
            return Ranking.FULL_HOUSE
        # Four-of-a-Kind — four dice showing the same value.
        if sorted(counts) == [1, 4]:
            return Ranking.FOUR_OF_A_KIND
        # Five-of-a-Kind — all five dice showing the same value.
        if sorted(counts) == [5]:
            return Ranking.FIVE_OF_A_KIND

    def compare_hands(self, hand1: list[int], hand2: list[int]):

        if self.evaluate_hand(hand1) > self.evaluate_hand(hand2):
            return "Player 1 is the winner!"
        elif self.evaluate_hand(hand2) > self.evaluate_hand(hand1):
            return "Player 2 is the winner!"
        else:
            return "It's a draw!"
