# Looping throught dictionaries.

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}

for key, value in user_0.items():       # item -> key-value pair
    print(f'\nkey: {key}')
    print(f'Value: {value}')