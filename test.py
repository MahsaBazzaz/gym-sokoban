import gymnasium as gym
import gym_sokoban

env = gym.make('Sokoban-sturgeon-v0', render_mode='rgb_array')
observation, info = env.reset(seed=None, options= None)
env.render()

action = env.action_space.sample()
print(action)
observation, reward, done, truncated, info = env.step(action)
print(observation)