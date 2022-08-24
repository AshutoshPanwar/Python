# Program to print vowels
# in word enter by the user

# Functioin define with no argument's
def search4vowels():
    """Display any vowel found in an asker-for word."""     # DocString
    vowel = set('aeiou')
    word = input("Provide a word to search for vowels: ")
    found = vowel.intersection(set(word))
    for vowel in found:
        print(vowel)

# Function Call
search4vowels()
