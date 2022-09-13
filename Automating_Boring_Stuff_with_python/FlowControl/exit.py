# Simple program to exit out of program
import sys

while True:
    print("Type exit to exit.")
    n = input(">")
    if n == 'exit':
        sys.exit()      # .exit() is used to exit out of program
    print("Try again!")