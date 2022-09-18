# Formatting text with rjust, ljust, center

def printPicinc(itemDict, leftWidth, rightWidth):
    print("PICNIC ITEMS".center(leftWidth + rightWidth, '-'))
    for k,v in itemDict.items():
        print(k.ljust(leftWidth,'.') + str(v).rjust(rightWidth))

picnicItems = {'sandwiches' : 4, 'apple' : 12, 'cups' : 4, 'cookies' : 8000}
printPicinc(picnicItems, 12, 5)
printPicinc(picnicItems, 20, 6)