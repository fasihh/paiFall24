class Animal:
    def __init__(self, name: str, age: int, habitat: str, available: bool):
        self.__name = name
        self.__age = age
        self.__habitat = habitat
        self.__available = available
    
    def set_status(self, available: bool):
        self.__available = available

    def info(self):
        print(f'Availability Status: {'Viewing' if self.__available else 'Quarantine'}')
        print(f'Name: {self.__name}')
        print(f'Age: {self.__age}')
        print(f'Habitat: {self.__habitat}')

class Mammal(Animal):
    def __init__(self, name: str, age: int, habitat: str, fur_length: int, diet: bool, available: bool = True):
        super().__init__(name, age, habitat, available)
        self.__fur_length = fur_length
        self.__diet = diet

    def info(self):
        print('Mammal:')
        super().info()
        print(f'Fur length: {self.__fur_length}')
        print(f'Diet: {'Carnivore' if self.__diet else 'Herbivore'}')

class Bird(Animal):
    def __init__(self, name: str, age: int, habitat: str, wing_span: int, altitude: int, available: bool = True):
        super().__init__(name, age, habitat, available)
        self.__wing_span = wing_span
        self.__altitude = altitude

    def info(self):
        print('Bird:')
        super().info()
        print(f'Wing span: {self.__wing_span}')
        print(f'Flying altitude: {self.__altitude}')

class Reptile(Animal):
    def __init__(self, name: str, age: int, habitat: str, scale_pattern: int, status: str, available: bool = True):
        super().__init__(name, age, habitat, available)
        self.__scale_pattern = scale_pattern
        self.__status = status

    def info(self):
        print('Reptile:')
        super().info()
        print(f'Scale Pattern #: {self.__scale_pattern}')
        print(f'Venomous Status: {'Venomous' if self.__status else 'Non-venomous'}')

mammal = Mammal('Mark', 5, 'Forest', 5, True)
reptile = Reptile('Zuck', 50, 'Swamp', 1, False)
bird = Bird('Berg', 2, 'Mountain', 20, 100)

info = lambda *animals: [[animal.info(), print()] for animal in animals]

print('BEFORE CHANGING STATUS')
info(mammal, reptile, bird)
mammal.set_status(False)
reptile.set_status(False)
print('AFTER CHANGING STATUS')
info(mammal, reptile, bird)
