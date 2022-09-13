# This is a guess the number game.

import random
secerete_Number = random.randint(1, 20)

print("I am thinking of a number between 1 and 20.")

for i in range(7):
    print("Guess the number.")
    guess = int(input())

    if guess < secerete_Number:
        print("Your guess is too low.")
    elif guess > secerete_Number:
        print("Your guess is too High.")
    else:
        break

if guess == secerete_Number:
    print("Good job! You guess the correct number in "+ str(i)+ "Guess")
else:
    print("The number I was thinking was ", secerete_Number)
    print("Please Try Again!")