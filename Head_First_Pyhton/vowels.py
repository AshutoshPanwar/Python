# Program to print vowels
# in word enter by the user

# Functioin define with argument's & return type
def search4vowels(word:str) -> str:
    """Display any vowel found in an asker-for word."""     # DocString
    vowel = set('aeiou')
    return vowel.intersection(set(word))

# Function Call
print(search4vowels('ashu'))
