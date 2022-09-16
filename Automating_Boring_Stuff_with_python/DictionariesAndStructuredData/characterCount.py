# Counrt no of times a character appera in a string
message = 'It was a bright cold day in April, and the clocks were striking thirteen.'
count = {}       # Empty Dict

for character in message:
    count.setdefault(character, 0)      # Add a new character to Dict
    count[character] = count[character] + 1     # Every time appera increment it's value

print(count)