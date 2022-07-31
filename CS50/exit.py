# Importing two functions form sys library
from sys import argv, exit

# Conditionals
if len(argv) != 2:          # In case no arguments are passed
    print("Command line argumeents are missing!")
    exit(1)                 # Exit program with error code

print(f"Hello, {argv[1]}")  # In case some arguments are passed
exit(0)                     # Exit program with success code