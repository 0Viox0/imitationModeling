from functionalBlocks.RequestsArrivalProcess import ArrivalProcess
from functionalBlocks.ServiceProcess import ServiceProcess
from functionalBlocks.QueueSystem import QueueSystem
from MersenneTwister import MersenneTwister
from DistributionSampler import DistributionSampler

class Simulation:
    def __init__(self, lambda_param, mean, stddev, queue_capacity, seed=None):
        self.generator = MersenneTwister(seed)
        self.arrival_process = ArrivalProcess(lambda_param, self.generator)
        self.service_process = ServiceProcess(mean, stddev, self.generator)
        self.queue_system = QueueSystem(queue_capacity, self.generator)
        
    def run(self, num_requests):
        time = 0
        for _ in range(num_requests):
            arrival_time = self.arrival_process.generate_arrival()
            time += arrival_time
            print(f"Заявка поступила в {time:.2f} времени.")
            
            # Проверка на очередь
            wait_time = self.queue_system.wait_in_queue()
            if wait_time == float('inf'):
                print(f"Очередь переполнена в {time:.2f}. Заявка отклонена.")
                continue
            else:
                print(f"Заявка ожидает {wait_time:.2f} времени в очереди.")
                
            # Обработка заявки
            service_time = self.service_process.process_request()
            time += service_time
            print(f"Заявка обработана за {service_time:.2f} времени. Общее время: {time:.2f}")