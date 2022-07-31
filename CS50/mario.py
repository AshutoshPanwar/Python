# Simple program to
# print a vertical
# wall of (#)


# Declaring main function
def main():
    height = get_height()       # Function call to get_height() function
    for i in range(height):
        print("#")


# Function for user input
def get_height():
    # Repeat till condition is true
    while True:
        # Exception Handling
        try:
            height = int(input("Hight: "))
            if height > 0:      # Condition
                break
        except ValueError:
            print("That not an integer!")
    return height               # Return Type


# Program Start to Execute for here
main()