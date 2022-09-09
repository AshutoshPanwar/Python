ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that. ")

stuff = ten_things.split(" ")       # Split string into list items
# List of items to push item to list that is short of items
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()     # Remove the last element from more_stuff and assigne it to next_one
    print("Adding: ", next_one)
    stuff.append(next_one)      # Push element to stuff list
    print(f"There are {len(stuff)} items now.")

print("There we go: ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop())
print(' '.join(stuff))      # Join list elements with space
print('#'.join(stuff[3:5]))     # Join list elements with #