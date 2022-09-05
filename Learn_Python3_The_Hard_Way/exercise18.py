# Different functions with different parameters

# Fun with two arguments
def print_two_again(arg1, arg2):
    print(f'arg1: {arg1}, arg2: {arg2}.')

# Fun with one argument
def print_one(arg1):
    print(f"arg1: {arg1}")

# Fun with no agruments
def print_none():
    print("I got nothing.")

# Fun calling
print_two_again("Ashu", "Panwar")
print_one('First!')
print_none()
