from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, make, model, year, mileage):
        self.make, self.model, self.year, self.mileage = make, model, year, mileage

    @abstractmethod
    def get_vehicle_info(self):
        pass
    @abstractmethod
    def increase_vehicle_mileage(self, amount):
        pass

    def calculate_depreciation(self, years):
        return 1000 * years
    
    @classmethod
    def create_new_vehicle(cls, make, model, year):
        return cls(make, model, year, 0)
    
class Car(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year, mileage)

    def get_vehicle_info(self):
        print(f'Car: {self.make}, {self.model}, {self.year}, Mileage: {self.mileage}')

    def increase_vehicle_mileage(self, amount):
        self.mileage += amount

class Truck(Vehicle):
    def __init__(self, make, model, year, mileage):
        super().__init__(make, model, year, mileage)

    def get_vehicle_info(self):
        print(f'Truck: {self.make}, {self.model}, {self.year}, Mileage: {self.mileage}')

    def increase_vehicle_mileage(self, amount):
        self.mileage += amount

if __name__ == '__main__':
    car, truck = Car('make1', 'model1', 2000, 100), Truck('make2', 'model2', 2001, 120)

    car.increase_vehicle_mileage(100), truck.increase_vehicle_mileage(100)

    car.get_vehicle_info(), truck.get_vehicle_info()

    print(car.calculate_depreciation(24), truck.calculate_depreciation(23), sep='\n')

    new_car, new_truck = Car.create_new_vehicle('make3', 'model3', 2002), Truck.create_new_vehicle('make4', 'model4', 2003)

    new_car.get_vehicle_info(), new_truck.get_vehicle_info()
