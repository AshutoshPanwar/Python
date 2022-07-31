# Program to convert
# string to uppercase

# Prompt user for input
before = input("Before: ")

# Print output
print("After: ", end="")
for c in before:
    print(c.upper(), end="")            # Each character to Uppercase
print()