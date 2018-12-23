import random
import numpy
import math
import gym
import sys
import tensorflow as tf

from keras import backend as k
from keras.models import Sequential
from keras.layers import *
from keras.optimizers import *

class Brain:
    def __init__(self, state_count, action_count):
        self.state_count = state_count
        self.action_count = action_count

        self.model = self._createModel()
        self.model_ = self._createModel()

    def _createModel(self):
        model = Sequential()

        model.add(Dense(units=64, activation='relu', input_dim=self.state_count))

class Environment:
    def __init__(self, problem):
        self.problem = problem
        self.env = gym.make(problem)

    def run(self, agent):
        # Setup a fresh environment and store it as a state in s
        s = self.env.reset()

        while True:
            a = agent.act(s)  # Decide what action to take in state s
            s_, r, done, info = self.env.step(a)

            if done:
                s_ = None

            agent.observe((s, a, r, s_))
            agent.replay()

            s = s_

            if done:
                break
