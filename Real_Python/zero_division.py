#! /usr/bin/python3

# Program to see the pracitical
# implementation of try and continue


def divide(num1, num2):
    try:
        print(num1 / num2)
    except TypeError:
        print("Both arguments must be numbers")
    except ZeroDivisionError:
        print("Num2 must not be zero")

divide(10, 2)
divide("asd", 2)    # Will raise content of TypeError block
divide(10, 0)       # Will raise content of ZeroDivisionError block