import random, sys

print('Rock, Paper, Scissors')

# Variables keep track of no of wins, loose and ties.
wins = 0
losses = 0
ties = 0

# The main loop
while True:
    print(f'{wins} Wins, {losses} Losses {ties} Ties')
    # The player input loop
    while True:     # Prompt for input until user don't enter frome one of the choice.
        print("Enter you move: (r)ock, (p)aper, (s)cissors or (q)uit.")
        # Taking user input
        playerMove = input(">")
        if playerMove == 'q':
            sys.exit()      # Quit the program
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break
        print("Type one of r, p, s, q.")

    # Display what the player chose:
    if playerMove == 'r':
        print("Rock versus...")
    elif playerMove == 'p':
        print("Paper vesus...")
    elif playerMove == 's':
        print("Scissors versus...")

    # Display what the computer choose
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print("Rock")
    elif randomNumber == 2:
        computerMove = 'p'
        print("Paper")
    elif randomNumber == 3:
        computerMove = 's'
        print("Scissors")

    # Display and recore win/loose/tie
    if playerMove == computerMove:
        print("It's a tie!")
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print("You Win!")
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print("You Win!")
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print("You Win!")
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print("You Lose!")
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print("You Lose!")
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print("You Lose!")
        losses = losses + 1
