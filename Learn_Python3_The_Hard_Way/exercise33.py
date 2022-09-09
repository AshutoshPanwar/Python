# Detail overview of how
# items are added with append
# to list using while loop

# initialize variables
i = 0
number = []


while i < 6:
    print(f"At the top i is {i}")       # Know the current value of i
    number.append(i)        # Add element to list
    i = i + 1       # Increment i by 1
    print("Numbers now: ", number)      # Show elements in the list
    print(f"At the bottom i is {i}")        # Know the incremented value of i

# Show the elements in the list
print("The number are: ")
for num in number:
    print(num)