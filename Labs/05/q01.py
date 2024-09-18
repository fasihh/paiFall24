from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, capacity):
        self.capacity = capacity

    @abstractmethod
    def get_fare(self):
        return self.capacity * 100
    
class Bus(Vehicle):
    def __init__(self, capacity):
        super().__init__(capacity)

    def get_fare(self):
        return super().get_fare() * 1.1

print(Bus(50).get_fare())
