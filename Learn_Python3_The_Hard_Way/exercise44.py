# Parent class
class Other(object):
    def override(self):
        print("Other override()")
    def implicit(self):
        print("Other implicit()")
    def altered(self):
        print("Other altered()")

# Creating Child class from Other
class Child(Other):
    def __init__(self):
        self.other = Other()
    # Referencing to implicit of parent class
    def implicit(self):
        self.other.implicit()
    def override(self):
        print("CHILD override()")
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

# creating object from class
son = Child()
# Calling class methods
son.implicit()
son.override()
son.altered()