from dice.dice_roll import DiceRoll
from hand_evaluation.evaluator import HandEvaluator
from betting.betting_mechanics import BettingMechanics
from decision_making.decision_logic import DecisionLogic


class Player:
    def __init__(self, name: str, dice_roll: DiceRoll, hand_evaluator: HandEvaluator):
        self.name = name
        self.dice_roll = dice_roll
        self.hand_evaluator = hand_evaluator
        self.result = []
        self.value = None
        self.reroll_indices = []

    def initial_roll(self):
        self.dice_roll.roll_dice()
        self.result = self.dice_roll.get_result()
        self.value = self.hand_evaluator.evaluate_hand(self.result)
        print(f"{self.name}'s initial roll: {self.result}")
        print(f"{self.name}'s hand value: {self.value}")

    def choose_reroll(self):
        reroll_input = input(
            f"{self.name}, enter the dice numbers (1-5) to re-roll, separated by spaces (or press Enter to keep all): ").strip()
        if not reroll_input:
            print(f"{self.name} is keeping all dice.")
            self.reroll_indices = []
        else:
            try:
                indices = [int(x) - 1 for x in reroll_input.split()]
                if all(0 <= idx < 5 for idx in indices):
                    self.reroll_indices = indices
                else:
                    print("Invalid input. Please enter numbers between 1 and 5.")
                    self.choose_reroll()
            except ValueError:
                print("Invalid input. Please enter valid numbers.")
                self.choose_reroll()

    def do_reroll(self):
        if self.reroll_indices:
            self.dice_roll.reroll_dice(self.reroll_indices)
            self.result = self.dice_roll.get_result()
            self.value = self.hand_evaluator.evaluate_hand(self.result)
            print(f"{self.name}'s new roll: {self.result}")
            print(f"{self.name}'s hand value: {self.value}")
        else:
            print(f"{self.name} kept all dice: {self.result}")


class GameSimulator:
    def __init__(self):
        self.hand_evaluator = HandEvaluator()
        self.betting_mechanics = BettingMechanics()
        self.decision_logic = DecisionLogic()
        self.players = [
            Player("Player 1", DiceRoll(), self.hand_evaluator),
            Player("Player 2", DiceRoll(), self.hand_evaluator)
        ]

    def game_loop(self):
        print("\n--- Initial Roll ---")
        for player in self.players:
            player.initial_roll()

        for _ in range(1, 3):
            print("\n--- Choose Dice to Re-roll ---")
            for player in self.players:
                player.choose_reroll()

            print("\n--- Re-rolling Dice ---")
            for player in self.players:
                player.do_reroll()

        print("\nComparing hands...")
        print(self.hand_evaluator.compare_hands(
            self.players[0].result, self.players[1].result))


if __name__ == "__main__":
    simulator = GameSimulator()
    simulator.game_loop()
