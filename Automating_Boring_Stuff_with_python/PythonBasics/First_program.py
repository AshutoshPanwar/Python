# This program says hello and asks for my name.

print("Hello, World!")
print("What's you name?")   # Ask's for user name

myName = input()
print("It's nice to meet you, " + myName)

print("The length of your name is: ")
print(len(myName))

print("What's you age?")    # Ask for user age
myAge = int(input())
print("You will be " + str(myAge+1) + " in a year")