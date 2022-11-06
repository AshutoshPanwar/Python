# Looping throught all keys in a Dictionary.

fav_language = {
    'jen': 'Java',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['jen', 'phil']

for names in fav_language.keys():
    if names in friends:
        print(f"{names.title()}, I see you love {fav_language[names].title()}")
    else:
        print(f"Hi, {names}")