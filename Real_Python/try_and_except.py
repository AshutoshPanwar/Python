#! /usr/bin/python3

# Program to see exception
# handeling in python

try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("That was not an integer")