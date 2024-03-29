# Setting default value, Modifying Attribute's value

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

my_new_car = Car('RR', 'Phantom', 2022)
print(my_new_car.get_descriptive_name())
my_new_car.odometer_reading = 23        # Modifying Attribute's value directly
my_new_car.read_odometer()
my_new_car.update_odometer(20_500)
my_new_car.read_odometer()
my_new_car.increment_odometer(100)
my_new_car.read_odometer()