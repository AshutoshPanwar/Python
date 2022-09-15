# Searching in list game

# List with elements
myPets = ['Lalu', 'Bruno', "Speed tail"]
prompt = '> '

print("Enter pet name:")
pet = input(prompt)

if pet in myPets:
    print(pet + ' is my pet.')
else:
    print("I do not have a pet.")