import gym
import random
import math
import tensorflow as tf

if __name__ == "__main__":
    env = gym.make("CartPole-v0")
    env.reset()

    for t in range(1000):
        env.render()

        action = env.action_space.sample()
        observation, reward, done, info = env.step(action)  # Random action

        print(observation, reward, info)
        if done:
            print("End of episode after {} timesteps".format(t + 1))
            break

    print(env.observation_space)
    print(env.action_space)
