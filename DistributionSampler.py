import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erfinv

class DistributionSampler:
    def __init__(self, generator):
        self.generator = generator
    
    def exponential(self, lambd):
        u = self.generator.genrand_float()
        return -np.log(1 - u) / lambd

    def normal(self, mu=0, sigma=1):
        u = self.generator.genrand_float()
        return mu + sigma * np.sqrt(2) * erfinv(2 * u - 1)
