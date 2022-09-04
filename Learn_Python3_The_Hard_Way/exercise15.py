# Read file data with file
# name passed in command line
from sys import argv

# Varibales to store command line arguments
script, filename = argv

# Open file
txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())       # print text from file

