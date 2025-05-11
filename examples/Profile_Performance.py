import cProfile
import gymnasium as gym
import gym_sokoban
import time
import argparse

parser = argparse.ArgumentParser(description='Run environment with random selected actions.')
parser.add_argument('--rounds', '-r', metavar='rounds', type=int,
                    help='number of rounds to play (default: 20)', default=20)
parser.add_argument('--env', '-e', metavar='env',
                    help='Environment to load (default: Sokoban-v0)', default='Sokoban-v0')
parser.add_argument('--render_mode', '-m', metavar='render_mode',
                    help='Render Mode (default: human)', default='human')

args = parser.parse_args()
env_name = args.env
n = args.rounds
render_mode = args.render_mode

cProfile.run('gym.make("{}")'.format(env_name), sort='time')

env = gym.make(env_name, render_mode=render_mode)

start = time.time()
for i in range(n):
    print('Reset {}/{}'.format(i+1, n))
    env.reset(seed=None,options= None)

end = time.time()
delta = end-start
hours, remainder = divmod(delta, 3600)
minutes, seconds = divmod(remainder, 60)
print('Done.\nReset {} times in {}:{}:{}'.format(n, int(hours), int(minutes), int(seconds)))
hours, remainder = divmod(delta*1.0/n, 3600)
minutes, seconds = divmod(remainder, 60)
print('Avg {}:{}:{}'.format(int(hours), int(minutes), seconds))
