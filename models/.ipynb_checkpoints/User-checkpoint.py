from DistributionSampler import DistributionSampler

class User:
    def __init__(self, user_id, generator, normal_mean=30, normal_std=5):
        self.user_id = user_id
        self.sampler = DistributionSampler(generator, normal_mean, normal_std)
    
    def decide_reading_time(self):
        return self.sampler.normal()