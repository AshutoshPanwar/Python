# Program to compare points

# Prompt user for input
points = int(input("How many points did you lose? "))

# Conditional statements
if points < 2:
    print("You Lose fewer points than me!")
elif points > 2:
    print("You lost more points than me!")
else:
    print("We loase the same points!")