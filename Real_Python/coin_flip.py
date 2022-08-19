# Practical implementation 
# of random function in python

#! /usr/bin/python3

import random

def coin_flip():
    """Random returnes head or tails"""
    if random.randint(0,1) == 0:
        return "Head"
    else:
        return "Tails"

count_head = 0
count_tail = 0

for toss in range(100):
    if coin_flip() == "Head":
        count_head = count_head + 1
    else:
        count_tail = count_tail + 1

print(count_head)
print(count_tail)

