import random

# Function define
def getAnswer(anserNumber):
    if anserNumber == 1:
        return "It is certain"
    elif anserNumber == 2:
        return "It is decidedly so"
    elif anserNumber == 3:
        return 'Yes'
    elif anserNumber == 4:
        return 'Reply hazy try again'
    elif anserNumber == 5:
        return 'Ask again later'
    elif anserNumber == 6:
        return "Concentrate and try again"
    elif anserNumber == 7:
        return "My reply is no"
    elif anserNumber == 8:
        return "Outlook not so good"
    elif anserNumber == 9:
        return 'Very doubtful'

# Calling function
r = random.randint(1,9)
print(getAnswer(r))
