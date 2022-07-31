# Program to take
# command line arguments


# Importing sys library
from sys import argv

# Print all the arguments entered by user
for arg in argv:
    if arg != "argv.py":        # Skip program name
        print(arg)