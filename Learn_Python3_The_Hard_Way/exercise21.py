# Parameterised function that return's some thing

# Function return Addition of two numbers
def add(a, b):
    print(f"Adding {a} + {b}.")
    return a+b

# Function return Subtraction of two numbers
def subtract(a, b):
    print(f"Subtract {a} - {b}.")
    return a-b

# Function return Multiplication of two numbers
def multiply(a, b):
    print(f"Multiply {a} * {b}.")
    return a*b

# Function return Division of two numbers
def divide(a, b):
    print(f"Divide {a} / {b}.")
    return a/b

print("Let's do some math with just function's!")

# Storing values returned by the function's
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

# Passing varibles with format()
print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes: ", what, "Can you do it by hand?")