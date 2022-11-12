# Inheritance

class Car:
    """A simple attemp to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to descibe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0       # Default Value
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.make} {self.model} {self.year}"
        return long_name.title()
    def read_odometer(self):
        """Print a statement showing the car's milage"""
        print(f"This car has {self.odometer_reading} miles on it.")
    def update_odometer(self,mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    def increment_odometer(self, miles):        # Incrementing value through Method
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)

my_tesla = ElectricCar('tesla', 'model S', 2019)
print(my_tesla.get_descriptive_name())