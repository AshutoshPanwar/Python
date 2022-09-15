# List are mutable

spam = [0, 1, 2, 3, 4, 5]
print(f"Spam: {spam}")
print("Id of spam: ")
print(id(spam))     # Both spam and cheese will have the same id
cheese = spam       # Python by default use reference
print('Id of cheese:')
print(id(cheese))       # Both spam and cheese will have the same id
print(f"Cheese: {cheese}")

print('After adding new element.')
cheese[1] = 100     # Replacing value at index 1
print(f"Spam: {spam}")
print(f"Cheese: {cheese}")

