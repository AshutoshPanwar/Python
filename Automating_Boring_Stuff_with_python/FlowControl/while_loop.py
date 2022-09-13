# Simple implementation of while loop and conditionals with a guessing game

name = ''

# while name != 'your name':
#     print("Please type your name.")
#     name = input()

# print("Thank You!")

while True:
    print("Who are you?")
    name = input()
    if name != 'ashu':
        continue
    print("Hello Sir, what is the password? (Top of the compay)")
    password = input()
    if password == 'CEO':
        break
print("Access Granted")