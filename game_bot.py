import gym
import universe

env = gym.make('flashgames.CoasterRacer-v0')
observayion_n = env.reset()

while True:
    action_n = [[('KeyEvent','ArrowUp',True)] for ob in observation_n]
    observation_n, reward_n, done_n, info = env.step(action_n)
    env.reader()
