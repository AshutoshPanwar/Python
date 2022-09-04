# Printing and taking input form user

print("How old are you?", end='')       # end keep the prompt on the same line
age = input()
print("How tall are you?", end='')
height = input()
print("How much do you weight?", end='')
weight = input()

# Passing variable with format()
print(f"So, you're {age} old, {height} tall and {weight} heavy.")