# Learn to create a class

# Dog is the class
class Dog:
    """A Simple sttemp to model a dog."""
    # Default method will execute for every instance of this class.
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    # These Method don't need additional information to run. So they just take (self) parameter.
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")
    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")

# Making Instance of a class
my_dog = Dog('Willie', 6)
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} year old.")