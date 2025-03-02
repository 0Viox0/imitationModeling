from DistributionSampler import DistributionSampler

class Librarian:
    def __init__(self, generator, normal_mean=2, normal_std=0.5):
        self.sampler = DistributionSampler(generator, normal_mean, normal_std)
        self.available_at = 0
        self.total_service_time = 0
    
    def serve_user(self, current_time):
        service_time = self.sampler.normal()
        self.total_service_time += service_time
        self.available_at = max(self.available_at, current_time) + service_time
        return self.available_at