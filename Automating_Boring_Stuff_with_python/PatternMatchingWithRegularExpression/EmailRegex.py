import re

emailRegex = re.compile(r'''(
    [a-zA-Z0-9._%+-]+           # username
    @                           # @ symbol
    [a-zA-Z0-9.-]+              # domain name
    (\.[a-zA-Z]{2,4})           # dot-something
    )''', re.VERBOSE)

text = input()

matches = []
for group in emailRegex.findall(text):
    matches.append(group[0])

if len(matches) > 0:
    print('Email is:')
    print('\n'.join(matches))
else:
    print("No phone number or email address found.")