# Program to print vowels
# in word enter by the user

# Functioin define with argument's
def search4vowels(word):
    """Display any vowel found in an asker-for word."""     # DocString
    vowel = set('aeiou')
    found = vowel.intersection(set(word))
    for vowel in found:
        print(vowel)

# Function Call
search4vowels('ashu')
