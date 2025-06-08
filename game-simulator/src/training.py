from stable_baselines3 import PPO
from stable_baselines3.common.monitor import Monitor
from dice_poker_env import DicePokerEnv, DicePokerEnv2


print("Starting Environment and Model")
env = DicePokerEnv2()
env = Monitor(env, "./logs")
policy_kwargs = dict(net_arch=[128, 128])  # PPO_2 [32, 32]; PPO_3 [64, 64]
model = PPO(policy="MlpPolicy",
            env=env,
            verbose=1,
            tensorboard_log="./ppo_tensorboard/",
            policy_kwargs=policy_kwargs,
            device="cpu")

print("Starting Training...")
model.learn(total_timesteps=500_000)
print("Finished Training.")

model.save("ppo_dice_poker")

# Test the trained agent
for k in range(0, 10):
    print(f"Starting game # {k}")
    obs, info = env.reset()
    print(f"Starting hand: {obs[:-1]}, value: {obs[-1]}")
    done = False
    while not done:
        action, _states = model.predict(obs, deterministic=True)
        print(f"Action: {action}")
        obs, reward, terminated, truncated, info = env.step(action)
        env.render()
        done = terminated or truncated

    print(f"Final reward: {reward}, Final hand value: {obs[-1]}")
    print()
