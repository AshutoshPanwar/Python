# Adding and mentanig birtyday data with Dictionaries in python

# Current data stored in Dict
birthdays = {'Alice' : 'Apr 1', 'Bob' : 'Dec 12', 'Carol' : 'Mar 4'}
prompt = '> '
while True:
    print("Enter a name: (blank to quit)")
    name = input(prompt)
    if name == '':      # Condition to exit out of program
        break

    if name in birthdays:       # if key found in Dict
        print(birthdays[name] + ' is the birthday of ' + name)
    else:       # Updating Dict of new user
        print("I don't have birthday information of " + name)
        print("What is their birthday?")
        bday = input()
        birthdays[name] = bday      # Adding Key-Value pair to Dict
        print('Birthday database updated')