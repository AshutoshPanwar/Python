# Infinite loop untill user enter a number
while True:
    print("Enter you age:")
    age = input()
    if age.isdecimal():
        break
    print("Please enter a number for you age.")

# Infinite loop until user enter a valid password
while True:
    print("Select a new password (letter and numbhers only):")
    password = input()
    if password.isalnum():
        break
    print("Passwords can only have letters and numbers.")