# Program to see exception
# handeling in python

#! /usr/bin/python3

try:
    number = int(input("Enter an integer: "))
except ValueError:
    print("That was not an integer")