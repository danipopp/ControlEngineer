import numpy as np

class MassSpringDamper:
    def __init__(self, m, c, k):
        self.m = m
        self.c = c
        self.k = k

    def dynamics(self, state, u):
        x, x_dot = state

        x_ddot = (u - self.c * x_dot - self.k * x) / self.m

        return np.array([x_dot, x_ddot])
