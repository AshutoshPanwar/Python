# Different ways of passing parameter's to function

# Function define
def cheese_and_crackers(cheese_cout, boxes_of_crackers):
    print(f"You have {cheese_cout} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party!")
    print("Get a blanket.\n")

print("We can just give the function numbers directly:")
cheese_and_crackers(20, 30)

print("Or, we can use variables from our script:")
amount_of_cheese = 10
amout_of_crackers = 50

# Passing values to fun with variables
cheese_and_crackers(amount_of_cheese, amout_of_crackers)

print("We can even do math inside too:")

# Function accept operation arguments
cheese_and_crackers(10 + 20, 5 + 6)

print("And we can combine the two, variables and math:")

# Passing values with variables + operation
cheese_and_crackers(amount_of_cheese + 100, amout_of_crackers + 1000)