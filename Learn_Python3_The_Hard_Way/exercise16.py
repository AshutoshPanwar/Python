# Erase all data of file and add new data to file entered by user

from sys import argv
script, filename = argv

# Display info to user
print(f"We're going to erase {filename}")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

# Waiting for user input
input("?")

# Openig file in write mode
print("Opening the file....")
target = open(filename, 'w')

# Erase all data of file with truncate() fun
print("Truncating the file. Goodbye!")
target.truncate()

# Display info to user
print("Now I'm going to ask you for three lines.")

# Taking input from user
line1 = input("line1: ")
line2 = input("line2: ")
line3 = input("line3: ")

# Display info to user
print("I'm going to write these to the file.")

# Writing each line to file
target.write(line1)
target.write("\n")      # We need to add manually to start from next line
target.write(line2)
target.write("\n")      # We need to add manually to start from next line
target.write(line3)
target.write("\n")      # We need to add manually to start from next line

# Don't forget to close the file after use.
print("And finally, We close it.")
target.close()