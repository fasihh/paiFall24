from abc import ABC, abstractmethod

CAR_RATE = 1.4
TRUCK_RATE = 1.8
SUV_RATE = 1.55

class Vehicle(ABC):
    def __init__(self, make, model, year, available):
        self.__make, self.__model, self.__year, self.__available = make, model, year, available

    def is_available(self):
        return self.__available
    
    def set_available(self, status):
        self.__available = status

    @abstractmethod
    def rentcost(self, duration):
        pass

    def info(self):
        print(f"MAKE: {self.__make}")
        print(f"MODEL: {self.__model}")
        print(f"YEAR: {self.__year}")
        print(f"STATUS: {"AVAILABLE" if self.__available else "NOT AVAILABLE"}")

class Car(Vehicle):
    def rentcost(self, duration):
        return duration * CAR_RATE

    def info(self):
        print("\tCAR")
        super().info()

class SUV(Vehicle):
    def rentcost(self, duration):
        return duration * SUV_RATE

    def info(self):
        print("\tSUV")
        super().info()

class Truck(Vehicle):
    def rentcost(self, duration):
        return duration * TRUCK_RATE

    def info(self):
        print("\tTRUCK")
        super().info()

class RentalReservation:
    def __init__(self, customer, vehicle, start, end):
        self.__customer, self.__vehicle, self.__start, self.__end = customer, vehicle, start, end
        self.__vehicle.set_available(False)

    def vehicle_info(self):
        print(f'START: {self.__start}')
        print(f'END: {self.__end}')
        print(f'COST: ${self.__vehicle.rentcost(abs(self.__end - self.__start))}')
        self.__vehicle.info()

class Customer:
    def __init__(self, name, contact):
        self.__name, self.__contact, self.__rented = name, contact, []

    def rent(self, reservation):
        self.__rented.append(reservation)

    def history(self):
        print(f"CUSTOMER NAME: {self.__name}")
        print(f"CUSTOMER CONTACT: {self.__contact}")
        print("HISTORY:")
        for rental in self.__rented:
            rental.vehicle_info()
            print()

car = Car('test_make_car', 'test_model_car', 2000, True)
suv = SUV('test_make_suv', 'test_model_suv', 2000, True)
truck = Truck('test_make_truck', 'test_model_truck', 2000, True)
customer = Customer("FASIH", "1234567890")
# start and end are numbers for the sake of simplicity
customer.rent(RentalReservation(customer, car, 0, 2))
customer.rent(RentalReservation(customer, truck, 1, 5))
customer.rent(RentalReservation(customer, truck, 3, 10))
customer.history()