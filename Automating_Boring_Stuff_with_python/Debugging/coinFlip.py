import random

heads = 0       # Initializing no of times head come.

for i in range(1, 1001):        # Flipping conin 1000 times.
    if random.randint(0,1) == 1:        # If head comes then increment head by one.
        heads = heads + 1
    if i == 500:        # Know half iteration is done.
        print("Halfway done!")

print("Heads come up " + str(heads) + ' times.')        # Print no of times head come in 1000 filps.