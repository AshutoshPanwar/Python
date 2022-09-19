#! python3
# Find Phone number

import re

phoneRegex = re.compile(r'''(
    (\d{3}|\(\d{3}\))?              # area code
    (\s|-|\.)?                      # seperator
    (\d{3})                         # first 3 digits
    (\s|-|\.)                       # separator
    (\d{4})                         # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
    )''',re.VERBOSE)

text = input()

matches = []
for group in phoneRegex.findall(text):
    phoneNum = '-'.join([group[1], group[3], group[5]])
    if group[8] != '':
        phoneNum += ' x' + group[8]
    matches.append(phoneNum)


if len(matches) > 0:
    print('Phone Number is:')
    print('\n'.join(matches))
else:
    print("No phone number or email address found.")