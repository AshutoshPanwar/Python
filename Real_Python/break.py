# Program to see 
# functionality of break 

#! /usr/bin/python3

n = 5

print("Inside the loop!")
for i in range(n):
    print("N =",i)
    if i == 2:
        break       # Break out of loop

print("Out side of loop!")
print("N =",n)