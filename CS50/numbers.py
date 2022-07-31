# Linear Search
# in python


# Import complete library
import sys

# Declaring list
number = [4, 6, 8, 10, 12, 0]

# Conditional statements
if 0 in number:         # By defalut python perform linear search
    print("Found!")
    sys.exit(0)         # Exit sucess code
else:
    print("Not Found!")
    sys.exit(1)         # Exit with error code