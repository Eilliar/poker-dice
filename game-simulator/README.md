# Dice Poker

https://witcher.fandom.com/wiki/The_Witcher_dice_poker

## Features

- **Dice Rolling**: Simulates rolling dice and retrieves the outcome.
- **Hand Evaluation**: Assesses the player's hand and determines the winner between two hands.
- **Betting Mechanics** [TBD]: Handles betting actions and resolves bets based on game outcomes.
- **Decision Making** [TBD]: Evaluates the game state to make informed decisions and assess risks.



## Running the Game

To start the game and run a Player vs Player experiment, execute the following command:

```bash
uv run src/main.py
```

Here is one example of gameplay:

```bash

--- Initial Roll ---
Player 1's initial roll: [2, 2, 5, 6, 6]
Player 1's hand value: 2
Player 2's initial roll: [4, 6, 3, 5, 1]
Player 2's hand value: 0

--- Choose Dice to Re-roll ---
Player 1, enter the dice numbers (1-5) to re-roll, separated by spaces (or press Enter to keep all): 3
Player 2, enter the dice numbers (1-5) to re-roll, separated by spaces (or press Enter to keep all): 5

--- Re-rolling Dice ---
Player 1's new roll: [2, 2, 1, 6, 6]
Player 1's hand value: 2
Player 2's new roll: [4, 6, 3, 5, 5]
Player 2's hand value: 1

--- Choose Dice to Re-roll ---
Player 1, enter the dice numbers (1-5) to re-roll, separated by spaces (or press Enter to keep all): 3
Player 2, enter the dice numbers (1-5) to re-roll, separated by spaces (or press Enter to keep all): 5

--- Re-rolling Dice ---
Player 1's new roll: [2, 2, 6, 6, 6]
Player 1's hand value: 6
Player 2's new roll: [4, 6, 3, 5, 6]
Player 2's hand value: 1

Comparing hands...
Player 1 is the winner!
```



## Training the agent:

Below are some examples of models trained and some of it's games after training. Keep in mind that for now, the agent learns to play by playing alone (single agent environment) and the idea is to check if it can learng the rules of the game through game play.

1. 
```python
policy_kwargs = dict(net_arch=[32, 32])
model = PPO(policy="MlpPolicy",
            env=env,
            verbose=1,
            policy_kwargs=policy_kwargs,
            device="cpu")
```
Starting game # 0
Starting hand: [3 2 6 2 1]
Action: [0. 0. 1. 0. 0.]
Hand: [3 2 4 2 1]
Action: [0. 0. 1. 0. 0.]
Hand: [3 2 4 2 1]
Final reward: 1

Starting game # 1
Starting hand: [6 2 2 2 1]
Action: [1. 0. 0. 0. 0.]
Hand: [2 2 2 2 1]
Action: [0. 0. 0. 0. 0.]
Hand: [2 2 2 2 1]
Final reward: 7

Starting game # 2
Starting hand: [6 5 2 1 2]
Action: [1. 1. 0. 0. 0.]
Hand: [3 5 2 1 2]
Action: [0. 1. 0. 0. 0.]
Hand: [3 5 2 1 2]
Final reward: 1

Starting game # 3
Starting hand: [2 6 1 5 4]
Action: [0. 1. 0. 1. 0.]
Hand: [2 3 1 5 4]
Action: [0. 0. 0. 1. 0.]
Hand: [2 3 1 6 4]
Final reward: 0

Starting game # 4
Starting hand: [3 2 1 5 4]
Action: [1. 0. 0. 1. 0.]
Hand: [1 2 1 3 4]
Action: [0. 0. 0. 1. 1.]
Hand: [1 2 1 2 4]
Final reward: 2

Starting game # 5
Starting hand: [1 2 2 3 3]
Action: [0. 0. 0. 1. 0.]
Hand: [1 2 2 5 3]
Action: [0. 0. 0. 1. 0.]
Hand: [1 2 2 2 3]
Final reward: 3

Starting game # 6
Starting hand: [1 2 2 3 5]
Action: [0. 0. 0. 0. 1.]
Hand: [1 2 2 3 3]
Action: [0. 0. 0. 1. 0.]
Hand: [1 2 2 6 3]
Final reward: 1

Starting game # 7
Starting hand: [5 6 2 1 2]
Action: [1. 1. 0. 0. 0.]
Hand: [6 4 2 1 2]
Action: [1. 0. 0. 0. 0.]
Hand: [3 4 2 1 2]
Final reward: 1

Starting game # 8
Starting hand: [4 2 3 6 2]
Action: [0. 0. 0. 1. 0.]
Hand: [4 2 3 1 2]
Action: [1. 0. 0. 0. 0.]
Hand: [1 2 3 1 2]
Final reward: 2

Starting game # 9
Starting hand: [6 2 5 3 4]
Action: [1. 0. 0. 0. 1.]
Hand: [2 2 5 3 3]
Action: [0. 0. 1. 0. 0.]
Hand: [2 2 3 3 3]
Final reward: 6


2. 
```python
policy_kwargs = dict(net_arch=[32, 32])
model = PPO(policy="MlpPolicy",
            env=env,
            verbose=1,
            policy_kwargs=policy_kwargs,
            device="cpu")

print("Starting Training...")
model.learn(total_timesteps=1_000_000)
```

Starting game # 0
Starting hand: [4 5 2 6 5]
Action: [0. 1. 0. 1. 1.]
Hand: [4 5 2 5 4]
Action: [0. 1. 0. 1. 0.]
Hand: [4 3 2 1 4]
Final reward: 1

Starting game # 1
Starting hand: [5 2 4 5 1]
Action: [1. 0. 1. 1. 0.]
Hand: [5 2 3 5 1]
Action: [1. 0. 0. 1. 0.]
Hand: [5 2 3 1 1]
Final reward: 1

Starting game # 2
Starting hand: [1 6 5 1 6]
Action: [0. 1. 1. 0. 1.]
Hand: [1 5 2 1 1]
Action: [0. 1. 1. 0. 0.]
Hand: [1 5 5 1 1]
Final reward: 6

Starting game # 3
Starting hand: [5 2 6 4 2]
Action: [1. 0. 1. 1. 0.]
Hand: [4 2 1 6 2]
Action: [1. 0. 0. 1. 0.]
Hand: [6 2 1 6 2]
Final reward: 2

Starting game # 4
Starting hand: [6 4 4 1 2]
Action: [1. 1. 1. 0. 0.]
Hand: [1 5 6 1 2]
Action: [0. 1. 1. 0. 1.]
Hand: [1 1 1 1 5]
Final reward: 7

Starting game # 5
Starting hand: [4 5 6 2 6]
Action: [0. 1. 1. 0. 1.]
Hand: [4 2 6 2 5]
Action: [1. 0. 1. 0. 1.]
Hand: [5 2 2 2 6]
Final reward: 3

Starting game # 6
Starting hand: [1 3 2 1 5]
Action: [0. 1. 0. 0. 1.]
Hand: [1 1 2 1 6]
Action: [0. 0. 1. 0. 1.]
Hand: [1 1 6 1 4]
Final reward: 3

Starting game # 7
Starting hand: [4 1 6 1 2]
Action: [1. 0. 1. 0. 0.]
Hand: [4 1 1 1 2]
Action: [1. 0. 0. 0. 1.]
Hand: [5 1 1 1 3]
Final reward: 3

Starting game # 8
Starting hand: [6 2 1 6 1]
Action: [1. 1. 0. 1. 0.]
Hand: [2 3 1 3 1]
Action: [0. 1. 0. 1. 0.]
Hand: [2 5 1 6 1]
Final reward: 1

Starting game # 9
Starting hand: [6 3 1 5 2]
Action: [1. 1. 0. 1. 0.]
Hand: [1 3 1 4 2]
Action: [0. 1. 0. 1. 0.]
Hand: [1 2 1 4 2]
Final reward: 2