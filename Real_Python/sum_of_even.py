# Program to find
# sum of all even number
# in range form 0 to 100

#! /usr/bin/python3

even = 0

for n in range(1,100):
    if n%2==0:
        even =even+n

print(even)
