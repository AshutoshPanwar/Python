#! /usr/bin/python3

# Program to see the
# practical implementation of
# try and except


num = -1

while num < 0:
    try:
        num = int(input("Enter the number: "))
    except ValueError:
        print("Try again")

