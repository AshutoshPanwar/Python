# Program to print vowels
# in word enter by the user

# Functioin define with argument's & return type
def search4vowels(word):
    """Display any vowel found in an asker-for word."""     # DocString
    vowel = set('aeiou')
    found = vowel.intersection(set(word))
    for vowel in found:
        return bool(found)

# Function Call
print(search4vowels('ashu'))
