# Local scope of variables inside functions

# Function define
def spam():
    eggs = 99
    bacon()
    print(eggs)
def bacon():
    ham = 101
    eggs = 0
    print(eggs)


# Function call
spam()