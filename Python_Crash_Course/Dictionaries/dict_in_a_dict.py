# Nested Dictionaries inside Dictionaries

users = {
    'aeinstein': {
        'first': 'alber',
        'last': 'einstein',
        'location': 'princeton',
    },
    'mcurie': {
        'first': 'merie',
        'last': 'curie',
        'location': 'paris',
    }
}

for username, user_info in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f'\t Full name: {full_name.title()}')
    print(f"\t Location = {location.title()}")