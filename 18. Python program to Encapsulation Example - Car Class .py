class Car:
    def __init__(self, make, model, year, mileage):
        self.__make = make
        self.__model = model
        self.__year = year
        self.__mileage = mileage

    # Getter methods
    def get_make(self):
        return self.__make

    def get_model(self):
        return self.__model

    def get_year(self):
        return self.__year

    def get_mileage(self):
        return self.__mileage

    # Setter methods
    def set_make(self, make):
        self.__make = make

    def set_model(self, model):
        self.__model = model

    def set_year(self, year):
        self.__year = year

    def set_mileage(self, mileage):
        self.__mileage = mileage

# Create an instance of the Car class
my_car = Car("Toyota", "Camry", 2007, 120000)

# Use the getter methods
print("Make:", my_car.get_make())
print
