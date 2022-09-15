# Python use references
# to create seperate copy we use .copy()

import copy

eggs = ['hello', 'tuples', 'immutable']
print("Id of eggs:")
print(id(eggs))     # eggs will have different ID

cheese = eggs.copy()
print("Id of cheese")
print(id(cheese))   # cheese will have different ID