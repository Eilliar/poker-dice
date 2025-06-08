import gymnasium as gym
import numpy as np
from gymnasium import spaces

from hand_evaluation.evaluator import HandEvaluator


class DicePokerEnv(gym.Env):
    metadata = {"render_modes": ["human"]}

    def __init__(self, max_rolls=3):
        super().__init__()
        self.observation_space = spaces.Box(
            low=1, high=6, shape=(5,), dtype=np.int32)
        self.action_space = spaces.MultiBinary(5)
        self.hand_evaluator = HandEvaluator()
        self.max_rolls = max_rolls
        self.current_roll = 0
        self.state = None
        self.prev_hand_value = 0

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = np.random.randint(1, 7, size=(5,), dtype=np.int32)
        self.current_roll = 1  # Initial roll counts as first roll
        self.prev_hand_value = self.hand_evaluator.evaluate_hand(
            self.state.tolist()).value
        return self.state.copy(), {}

    # def step(self, action):
    #     # action: binary mask for dice to re-roll
    #     for i in range(5):
    #         if action[i]:
    #             self.state[i] = np.random.randint(1, 7)
    #     self.current_roll += 1

    #     if self.current_roll >= self.max_rolls:
    #         # Episode over, evaluate hand
    #         hand_value = self.hand_evaluator.evaluate_hand(self.state.tolist())
    #         reward = hand_value.value  # Reward is the hand ranking value
    #         terminated = True
    #     else:
    #         reward = 0
    #         terminated = False

    #     truncated = False
    #     info = {"hand": self.state.copy()}
    #     return self.state.copy(), reward, terminated, truncated, info

    def step(self, action):
        # action: binary mask for dice to re-roll
        for i in range(5):
            if action[i]:
                self.state[i] = np.random.randint(1, 7)
        self.current_roll += 1

        new_hand_value = self.hand_evaluator.evaluate_hand(
            self.state.tolist()).value
        # reward = new_hand_value - self.prev_hand_value
        reward = new_hand_value
        self.prev_hand_value = new_hand_value

        if self.current_roll >= self.max_rolls:
            terminated = True
        else:
            terminated = False

        truncated = False
        info = {"hand": self.state.copy()}
        return self.state.copy(), reward, terminated, truncated, info

    def render(self, mode="human"):
        print(f"Hand: {self.state}")

    def close(self):
        pass

class DicePokerEnv2(gym.Env):
    metadata = {"render_modes": ["human"]}

    def __init__(self, max_rolls=3):
        super().__init__()
        # 5 dice (1-6) + 1 hand value (0-8, assuming 9 hand ranks)
        self.observation_space = spaces.Box(
            low=np.array([1, 1, 1, 1, 1, 0]),
            high=np.array([6, 6, 6, 6, 6, 8]),
            shape=(6,),
            dtype=np.int32
        )
        self.action_space = spaces.MultiBinary(5)
        self.hand_evaluator = HandEvaluator()
        self.max_rolls = max_rolls
        self.current_roll = 0
        self.state = None
        self.first_hand_value = 0

    def _get_obs(self):
        hand_value = self.hand_evaluator.evaluate_hand(self.state.tolist()).value
        return np.array(list(self.state) + [hand_value], dtype=np.int32)

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.state = np.random.randint(1, 7, size=(5,), dtype=np.int32)
        self.current_roll = 1
        self.first_hand_value = self.hand_evaluator.evaluate_hand(self.state.tolist()).value
        return self._get_obs(), {}

    def step(self, action):
        for i in range(5):
            if action[i]:
                self.state[i] = np.random.randint(1, 7)
        self.current_roll += 1

        hand_value = self.hand_evaluator.evaluate_hand(self.state.tolist()).value
        obs = np.array(list(self.state) + [hand_value], dtype=np.int32)

        if self.current_roll >= self.max_rolls:
            reward = hand_value  - self.first_hand_value # Only final reward
            terminated = True
        else:
            reward = 0
            terminated = False

        truncated = False
        info = {"hand": self.state.copy(), "hand_value": hand_value}
        return obs, reward, terminated, truncated, info

    def render(self, mode="human"):
        hand_value = self.hand_evaluator.evaluate_hand(self.state.tolist()).value
        print(f"Hand: {self.state}, value: {hand_value}")

    def close(self):
        pass