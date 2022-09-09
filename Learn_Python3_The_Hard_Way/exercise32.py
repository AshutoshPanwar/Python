# List in python

# List are denoted by [] brackets.
the_count = [1,2,3,4,5]
fruits = ['apple', 'orange', 'pears', 'apricote']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# Iterating to each item in a list with for loop
for num in the_count:
    print(f"This is count {num}")

for fruit in fruits:
    print(f"A fruit is of type: {fruit}")

for i in change:
    print(f"I got {i}")

# Declaring empty list
elements = []
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    elements.append(i)      # Add element (i) to list

for i in elements:
    print(f"Element was: {i}")