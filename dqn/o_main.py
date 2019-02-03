import math
import random
import gym
import tensorflow as tf
import numpy as np

class Environment:
    def __init__(self, p):
        self.problem = p
        self.env = gym.make(problem)
