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

print(coin_flip())
print(coin_flip())
print(coin_flip())
print(coin_flip())
print(coin_flip())
