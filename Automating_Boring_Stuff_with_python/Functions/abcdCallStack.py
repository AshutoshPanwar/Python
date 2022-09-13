# Function define
def a():
    print("a() starts")
    b()     # Reference to b() function
    d()     # Reference to d() function
    print("a() returns")

def b():
    print("b() starts")
    c()     # Reference to c() function
    print("b() returns")

def c():
    print("c() starts")
    print("c() returns")

def d():
    print("d() starts")
    print("d() returns")

# Function call
a()