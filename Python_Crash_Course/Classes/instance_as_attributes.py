# We break a large class into smaller classes that work together.

class Car:
    """A simple attemp to represent a car."""
    def __init__(self, make, model, year):
        """Initialize attributes to descibe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
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
    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles

class Battery:
    """A simple attemp to model a battery for an electic car."""
    def __init__(self, battery_size = 75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size
    def describe_battery(self):
        """Print a statement describing the bettery size."""
        print(f"This car has a {self.battery_size}-KWH battery.")
    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
        print(f"This car can go about {range} miles on a full charge.")

class ElectircCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        super().__init__(make, model, year)
        self.battery = Battery()        # Class call

my_tesla = ElectircCar('tesla', 'model S', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()