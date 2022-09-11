# Speaking Class in python

## Animal is-a object
class Animal(object):
    pass

## Dog has-a __init__ that take self and name as parameter
class Dog(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

## Cat has-a __init__ that take self and name as parameter:
class Cat(Animal):
    def __init__(self, name):
        ## ??
        self.name = name

class Person(object):
    def __init__(self, name):
        ## ??
        self.name = name
        ## Person has-a pet of some kind
        self.pet = None

class Employee(Person):
    def __init__(self, name, salary):
        ## ?? jmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## ??
        self.salary = salary

# Making a class Fish that is-a object
class Fish(object):
    pass

# Making a class Salmon that is-a Fish
class Salmon(Fish):
    pass

# Making a class Halibut that is-a Fish
class Halibut(Fish):
    pass

## rover is-a Dog
rover = Dog("Rover")

# sata is-a Cat
satan = Cat("Satan")

# mary is-a Person
mary = Person("Mary")

# mary has-a pet
mary.pet = satan

# frank is-a Employee
frank = Employee("Frank", 120000)

# frank has-a pet
frank.pet = rover

# flipper is-a fish
flipper = Fish()

# crouse is-a Salmon
crouse = Salmon()

# harry is-a Halibut
harry = Halibut()

