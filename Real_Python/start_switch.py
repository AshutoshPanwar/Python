# Program to find item
# in list start with 'be'

# Declearing List
list = ['Become', "become", "Bear", 'bEautifull']

for i in range(len(list)):
    list[i] = list[i].startswith('be')  # Return True If Found

# outPut the new List
print(list)