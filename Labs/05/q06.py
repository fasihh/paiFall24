from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    @abstractmethod
    def calculate_bonus(self):
        pass

class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def hire(self):
        print(f'{self.name} is hiring...')

    def calculate_bonus(self):
        return self.salary * 0.2

class Developer(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def write_code(self):
        print(f'{self.name} is writing code...')

    def calculate_bonus(self):
        return self.salary * 0.1
    
class SeniorManager(Manager):
    def __init__(self, name, salary):
        super().__init__(name, salary)

    def calculate_bonus(self):
        return super().calculate_bonus() * 1.5

print(Developer('ali', 727).calculate_bonus())
print(Manager('owais', 1200).calculate_bonus())
print(SeniorManager('fasih', 1200).calculate_bonus())