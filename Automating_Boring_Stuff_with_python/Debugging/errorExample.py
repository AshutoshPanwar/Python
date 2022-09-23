# Traceback error

# Functio define
def spam():
    bacon()     # Function call

# Function define
def bacon():
    raise Exception("This is the error message.")

spam()      # Function call