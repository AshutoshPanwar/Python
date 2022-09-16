allGuests = {'Alice' : {'apple' : 5, 'pretxelx' : 12},
            'bob' : {'ham sandwiches' : 3, 'apple' : 2},
            'carol' : {'cups' : 3, 'apple pies' : 1}}

def totalBrought(guests, item):
    numBrought = 0
    for k, v in guests.items():
        numBrought = numBrought + v.get(item, 0)        # Count no of times a item appeared
    return numBrought

print("Number of things being brought:")
print(" -Apples         " + str(totalBrought(allGuests, 'apple')))
print(" -Cups           " + str(totalBrought(allGuests, 'cups')))
print(" -Cakes          " + str(totalBrought(allGuests, 'cakes')))
print(" -Ham Sandwiches " + str(totalBrought(allGuests, 'ham sandwiches')))
print(" -Apple Pies     " + str(totalBrought(allGuests, 'apple pies')))