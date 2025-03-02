import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfinv

class DistributionSampler:
    def __init__(self, generator, normal_mean=0, normal_std=1):
        self.generator = generator
        self.normal_mean = normal_mean
        self.normal_std = normal_std
    
    def exponential(self, lambd):
        u = self.generator.genrand_float()
        return -np.log(1 - u) / lambd

    def normal(self):
        u = self.generator.genrand_float()
        return self.normal_mean + self.normal_std * np.sqrt(2) * erfinv(2 * u - 1)