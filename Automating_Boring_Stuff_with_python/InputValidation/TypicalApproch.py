# Naive approch of taking valid input.

while True:
    print("Enter you age:")
    age = input()
    try:
        age = int(age)
    except:
        print("Please use numeric digits.")
        continue
    if age < 1:
        print("Please enter a positive number.")
        continue
    break

print(f'You age is {age}')