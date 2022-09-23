# This program prints box and raise exception if wrong or invalid parametes are provided.

# Function define
def boxPrint(symbol, width, height):
    # Rasise exception if there is problem with parametes
    if len(symbol) != 1:
        raise Exception("Symbol must be a single character string.")
    if width <= 2:
        raise Exception("Width must be greater than 2.")
    if height <= 2:
        raise Exception("Height must be greater than 2.")
    # If every thing is fine.
    print(symbol * width)       # Top box line
    for i in range(height -2):
        print(symbol + (' '*(width - 2)) + symbol)
    print(symbol * width)       # Bottom box line

# Function call
for sym, w, h in (('*', 4, 4), ('0', 20, 5), ('x', 1, 3), ('ZZ', 3, 3)):        # Passing multiple parameters with for loop
    try:
        boxPrint(sym, w, h)
    except Exception as err:
        print("An Exception Happened: " + str(err))