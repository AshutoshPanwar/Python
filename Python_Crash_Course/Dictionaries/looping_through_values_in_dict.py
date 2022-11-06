# Looping throught all values in a Dictionaries.

fav_language = {
    'jen': 'Java',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

print("The following langauges have been mentioned:")
for lang in fav_language.values():
    print(lang.title())