try:
    x = int(input("X: "))
except ValueError:
    print("Thats not an int!")
    exit()
try:
    y = int(input("Y: "))
except ValueError:
    print("Thats not an int!")
    exit()

print(x+y)
