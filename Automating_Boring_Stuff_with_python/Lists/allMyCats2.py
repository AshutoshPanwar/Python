# List make life easy

# Declearing empty list
CatName = []

while True:
    print("Enter the name of cat " + str(len(CatName) + 1) + ' (Or enter nothing to stop.):')
    name = input()      # Taking user input
    if name == '':      # Condition to exit the loop
        break
    CatName += name     # Add element to list

# See all items in list
print("The cat names are:")
for name in CatName:
    print(' ' + name)